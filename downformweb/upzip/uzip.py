__author__ = 'root'


from zipfile import ZipFile,ZIP_DEFLATED
import os
import logging
import time

logging.basicConfig(filename="zip.log")

def extract_zip(filename, save_path):
    try:
        with ZipFile(filename, "r") as archive:
            try:
                archive.extractall(path=save_path, pwd="infected")
                os.remove(filename)
            except Exception, e:
                logging.error(time.ctime()+'\t'+str(e))
    except Exception,e:
        logging.error(time.ctime()+'\t'+str(e))


if __name__ == '__main__':
    filepath = '/root/data/test.zip'
    save_path = '/root/data/'
    extract_zip(filepath,save_path)
