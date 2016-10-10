__author__ = 'root'

from flask import Flask,make_response,send_file
from flaskdb.flaskdb import *
import os

app = Flask(__name__)

@app.route('/reset')
def reset():
    fdb = FlaskDb('./malspider/malspider/md5.db')
    fdb.resetall()
    return "reset flag to False"


@app.route('/download')
def download():
    fdb = FlaskDb('./malspider/malspider/md5.db')
    filename = fdb.selectData()
    path = '/root/data'
    filepath = os.path.join(path, filename)
    try:
        response = make_response(send_file(filepath))
        response.headers["Content-Disposition"] = "attachment; filename=%s"%filename
        fdb.updataFlag(md5=filename)
    except Exception,e:
        print Exception,':',e
        #need add log code
    finally:
        return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')