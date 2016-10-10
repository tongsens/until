__author__ = 'root'

import sqlite3

class FlaskDb():
    def __init__(self, dbpath):
        try:
            self.cx = sqlite3.connect(dbpath)
            self.cu = self.cx.cursor()
        except Exception,ex:
            print Exception,':',ex

    def selectData(self):
        try:
            select_data = 'SELECT md5 FROM md5 WHERE isdown = 0 LIMIT 1'
            self.cu.execute(select_data)
            res = self.cu.fetchall()
            return res[0][0]
        except Exception,e:
            print Exception,':',e

    def updataFlag(self, md5=None):
        try:
            updata_cmd = 'UPDATE md5 SET isdown = 1 WHERE md5="%s"'%md5
            self.cu.execute(updata_cmd)
            self.cx.commit()
        except Exception,e:
            print Exception,':',e

    def resetall(self):
        try:
            updata_all = 'UPDATE md5 SET isdown = 0'
            self.cu.execute(updata_all)
            self.cx.commit()
        except Exception,e:
            print Exception,':',e

if __name__ == '__main__':
    fdb = FlaskDb('../malspider/malspider/md5.db')
    fdb.resetall()
