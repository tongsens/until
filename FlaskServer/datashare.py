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
    tar_file = zip_dir(targetpath, '/root/tmp.zip')
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
    with open('/root/writebuf', 'w') as fp:
        fp.write(data)
    return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001, threaded=True)