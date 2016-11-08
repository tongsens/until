__author__ = 'root'

import pandas as pd
import sqlite3

def read_data(filename, dict):
    dga1 = pd.read_csv(filename)
    for domain in dga1["domain"]:
        if domain in dict.keys():
            dict[domain] += 1
        else:
            dict[domain] = 1

def test():
    count_dict = {}
    read_data("urldga2.csv", count_dict)
    read_data("urlinf2.csv", count_dict)
    read_data("urlsd2.csv", count_dict)
    result = sorted(count_dict.iteritems(), key=lambda dd:dd[1], reverse=True)
    for res in result:
        print res


def create_table():
    cx = sqlite3.connect("domain.db")
    cu = cx.cursor()
    try:
        crate_table = "CREATE TABLE IF NOT EXISTS domains (url TEXT UNIQUE, domains TEXT, class TEXT)"
        cu.execute(crate_table)
        cx.commit()
            #logging.info(time.ctime()+crate_table)
    except Exception,e:
        print Exception,e
    finally:
        cu.close()
        cx.close()

def save_data(filename):
    data_frame = pd.read_csv(filename)
    cx = sqlite3.connect("domain.db")
    cu = cx.cursor()
    for data in data_frame.values:
        indata = tuple(data[1:])
        try:
            insert_cmd = 'INSERT INTO domains(url, domains, class) VALUES ("%s","%s","%s")'%indata
            cu.execute(insert_cmd)
            cx.commit()
        except Exception,e:
            print Exception,e
    cu.close()
    cx.close()

def build_db():
    create_table()
    save_data('urldga2.csv')
    save_data('urlinf2.csv')
    save_data('urlsd2.csv')

if __name__ == '__main__':
    build_db()