__author__ = 'root'

import sqlite3
import time
import logging
import sys

logging.basicConfig(filename="db.log", level=logging.INFO)


class DataBase():
    def __init__(self, dbpath):
        try:
            self.cx = sqlite3.connect(dbpath)
            self.cu = self.cx.cursor()
        except Exception,e:
            logging.error(sys._getframe().f_code.co_name+str(e))
        self.dbInit()

    def dbInit(self):
        try:
            crate_table = "CREATE TABLE IF NOT EXISTS md5 (id INTEGER PRIMARY KEY, md5 TEXT UNIQUE, isdown INTEGER)"
            self.cu.execute(crate_table)
            self.cx.commit()
            #logging.info(time.ctime()+crate_table)
        except Exception,e:
            logging.error(sys._getframe().f_code.co_name+'::'+str(e))

    def insertMd5(self, md5=None):
        try:
            insert_data = 'INSERT INTO md5(md5, isdown) VALUES ("%s", 0)'%md5
            self.cu.execute(insert_data)
            self.cx.commit()
            logging.info(insert_data)
        except Exception,e:
            logging.error(sys._getframe().f_code.co_name+'::'+str(e))

    def isExit(self, md5=None):
        flag = False
        try:
            select_data = 'SELECT COUNT(*) FROM md5 WHERE md5 = "%s"'%md5
            self.cu.execute(select_data)
            res = self.cu.fetchall()
            if 1 in res[0]:
                flag = True
        except Exception,e:
            logging.error(sys._getframe().f_code.co_name+'::'+str(e))
        finally:
            return flag

    def __del__(self):
        self.cu.close()
        self.cx.close()


if __name__ == '__main__':
    db = DataBase('md5.db')
    db.insertMd5(md5='skfjkd111')