__author__ = 'root'

from flask import Flask,make_response,send_file
import os
import zipfile

app = Flask(__name__)


def zip_dir(dirname, zipfilename):
    '''
    :param dirname: source name
    :param zipfilename: targetfilename
    :return: target file path
    '''
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.close()
    return zipfilename

@app.route('/downfile/<path>')
def downfile(path):
    '''
    download path
    :param path: filepath
    :return:
    '''
    pathlist = path.split('*')
    targetpath = os.path.join('/', *pathlist)
    tar_file = zip_dir(targetpath, '/root/datashare/tmp.zip')
    try:
        response = make_response(send_file(tar_file))
        response.headers["Content-Disposition"] = "attachment; filename=tmp.zip"
    except Exception,e:
        print Exception,':',e
            #need add log code
    finally:
        return response

@app.route('/read/<path>')
def readfile(path):
    '''
    read linux file to web page
    :param path: linux file we want
    :return: file buf
    '''
    pathlist = path.split('*')
    targetfile = os.path.join('/', *pathlist)
    with open(targetfile, 'r') as fp:
        buf = fp.read()
    return buf

@app.route('/write/<data>')
def writefile(data):
    '''
    user upload , and to copy borad
    :param data: user input
    :return: input
    '''
    filepath = '/root/datashare/writebuf'
    with open(filepath, 'w') as fp:
        fp.write(data)
    cmd = 'cat %s | xclip -selection clipboard'%filepath
    os.system(cmd)
    return data


@app.route('/paste')
def paste():
    '''
    get paste data
    :return: paste data
    '''
    return os.popen('xclip -o').read()


@app.route('/')
def index():
    usage = '''
        <html>
        <body>
        <h1>usage:</h1>
        <p>/paste</p>
        <p>/read/path  path split by *, ex:root*tmp=/root/tmp</p>
        <p>/write/data</p>
        <p>/download/path</p>
        <body>
        </html>
        '''
    return usage


if __name__ == '__main__':
    try:
        os.system('mkdir /root/datashare')
    except Exception,e:
        print e
    app.debug = True
    app.run(host='0.0.0.0', port=5002, threaded=True)