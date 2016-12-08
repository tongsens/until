__author__ = 'root'

import pymongo
from collections import Counter

class GetData():
    def __init__(self):
        db = pymongo.MongoClient(host="192.168.99.215", port=27017)
        self.db_handler = db.cuckooinf.analysis
        self.create = []
        self.delete = []

    def get_result(self):
        json_list = self.db_handler.find().limit(5000)
        return json_list

    def get_item(self, sample, kee=None, *keys):
        try:
            rets = sample
            for key in keys:
                rets = rets[key]
            if kee!=None:
                rets = [d[kee] for d in rets]
            return rets
        except Exception,e:
            #print Exception,e
            return None

    def getdata(self):
        json_list = self.get_result()
        for sample in json_list:
            key_list1 = ['behavior', 'summary', 'file_created']; kee=None
            key_list2 = ['behavior', 'summary', 'file_deleted']; kee=None
            create_list =  self.get_item(sample, kee, *key_list1)
            if create_list:
                for cre in create_list:
                    crestr = cre.encode('utf-8').lower()
                    self.create.append(crestr)
            delete_list =  self.get_item(sample, kee, *key_list2)
            if delete_list:
                for dele in delete_list:
                    delstr = dele.encode('utf-8').lower()
                    self.delete.append(delstr)

    def count(self, datalist, level=2):
        counter = Counter()
        tmp_create = []
        for data in datalist:
            dirlist =  data.split('\\')
            if len(dirlist)>level:
                tmpdir = '\\'.join(dirlist[:level])
                tmp_create.append(tmpdir)
        counter.update(tmp_create)
        result = sorted(counter.items(), key=lambda f:f[1], reverse=True)
        return result

    def buildtree(self, data, xlist, i):
        if len(xlist)==0:
            return
        print ''.center(i*4, '-') , i ,data
        i += 1
        keyy = data[0]
        for data in xlist[0]:
            if keyy in data[0]:
                self.buildtree(data, xlist[1:], i)


    def doit(self):
        print 'create'
        create_list = []
        for i in range(2,8):
            create_list.append(self.count(self.create, level=i))
        for data in create_list[0]:
            self.buildtree(data, create_list[1:], 0)
        print 'delete'
        del_list = []
        for i in range(2,8):
            del_list.append(self.count(self.delete, level=i))
        for data in del_list[0]:
            self.buildtree(data, del_list[1:], 0)


    def printdata(self):
        for data in self.create:
            print data
        print ''.center(40, '-')
        for data in self.delete:
            print data

if __name__ == '__main__':
    gdata = GetData()
    gdata.getdata()
    gdata.doit()