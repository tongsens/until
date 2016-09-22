__author__ = 'root'
import requests
import json
import os
import time
import hashlib
import sqlite3

class Cuckoo():
    def __init__(self):
        pass

    def getstatus(self, ip_list):
        REST_URL = "http://%s:8090/machines/list"
        json_decoder = json.JSONDecoder()
        free_ip = []
        for ip in ip_list:
            url = REST_URL%ip
            try:
                request = requests.get(url)
                locked = json_decoder.decode(request.text)['machines'][0]['locked']
                if not locked:
                    free_ip.append(ip)
                    print ip,'is free'
            except:
                print url,'404'
        return free_ip

    def deltask(self, ip_list):
        REST_URL = "http://%s:8090/tasks/list"
        json_decoder = json.JSONDecoder()
        for ip in ip_list:
            url = REST_URL%ip
            try:
                request = requests.get(url)
                task_list = json_decoder.decode(request.text)["tasks"]
                for task in task_list:
                    task_id = task['id']
                    status = task['status']
                    if status == 'reported':
                        self.dodel(ip, task_id)
            except:
                pass

    def dodel(self, ip, task_id):
        url = "http://%s:8090/tasks/delete/%d"%(ip,task_id)
        try:
            requests.get(url)
            print url
        except:
            pass

    def submit(self, ip ,file):
        REST_URL = "http://%s:8090/tasks/create/file"%ip
        with open(file, "rb") as fp:
            multipart_file = {"file":("tmpfile", fp)}
            try:
                request = requests.post(REST_URL, files=multipart_file)
                print REST_URL
            except:
                pass

class FileOp():
    def __init__(self):
        self.filepath = self.readconf()

    def readconf(self):
        with open('filepath.conf', 'r') as fp:
            buf = fp.read()
        return buf

    def getfile(self):
        filelist = os.listdir(self.filepath)
        fpath = os.path.join(self.filepath, filelist[0])
        return fpath

    def delfile(self, filepath):
        try:
            os.remove(filepath)
            print "del %s success"%filepath
        except:
            print "del %s failed"%filepath

def readip():
    with open('cuckooip.conf', 'r') as fp:
        buf = fp.read()
    ip_list = buf.split('\n')
    return ip_list

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('md5.db')
        try:
            self.conn.execute("CREATE TABLE md5 (md5 TEXT NOT NULL UNIQUE)")
        except:
            pass

    def calcmd5(self, filename):
        with open(filename, 'rb') as fp:
            md5obj = hashlib.md5()
            md5obj.update(fp.read())
            hashvalue = md5obj.hexdigest()
        return hashvalue

    def insert(self, md5value):
        cmd = "INSERT INTO md5 VALUES ('%s')"%md5value
        try:
            self.conn.execute(cmd)
            self.conn.commit()
            return True
        except:
            print 'file exit'
            return False


def main():
    ip_list = readip()
    cuckoo = Cuckoo()
    fop = FileOp()
    db = Database()
    while True:
        free_iplist = cuckoo.getstatus(ip_list)
        for ip in free_iplist:
            try:
                filepath = fop.getfile()
                filemd5 = db.calcmd5(filepath)
                if db.insert(filemd5):
                    cuckoo.submit(ip, filepath)
                fop.delfile(filepath)
            except:
                pass
        cuckoo.deltask(ip_list)
        time.sleep(10)

def test():
    fop = FileOp()
    filename =  fop.getfile()
    db =Database()
    md5value = db.calcmd5(filename)
    db.insert(md5value)

if __name__ == '__main__':
    main()
    #test()