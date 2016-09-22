__author__ = 'root'


def mmsearch(filepath):
    with open(filepath, 'rb') as fp:
        buf = fp.read()
    print buf

if __name__ == '__main__':
    filepath = '/root/core/core'
    mmsearch(filepath)