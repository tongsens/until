__author__ = 'root'


import os
import sqlite3

def filelist(dirpath):
    c = 0
    for file in os.listdir(dirpath):
        if isExit(file):
            pass
        else:
            fpath = os.path.join(dirpath, file)
            cmd = "cp %s /root/data"%fpath
            print cmd
            os.system(cmd)
            c += 1
    print c


def isExit(md5):
    cx = sqlite3.connect('md5_inf.db')
    cu = cx.cursor()
    flag = False
    try:
        select_data = 'SELECT COUNT(*) FROM md5 WHERE md5 = "%s"'%md5
        cu.execute(select_data)
        res = cu.fetchall()
        if 1 in res[0]:
            flag = True
    except Exception,e:
        pass
    finally:
        return flag
        cu.close()
        cx.close()


if __name__ == '__main__':
    path = '/mnt/data'
    filelist(path)