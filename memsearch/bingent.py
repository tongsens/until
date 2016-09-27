__author__ = 'root'


def ischr(ch):
    if ch in range(0x30, 0x3a):
        return True
    if ch in range(0x41,0x47):
        return True
    if ch in range(0x61, 0x67):
        return True
    return False

def readfile(filename):
    with open(filename, 'r') as fp:
        buf = fp.read()
    tmpstr = []
    for ch in buf:
        if ischr(ord(ch)):
            tmpstr.append(ch)
    retlist = []
    for i in range(0, len(tmpstr), 2):
        retlist.append(tmpstr[i]+tmpstr[i+1])
    return retlist

def filewrite(buf):
    with open('/root/tmp/test.bin', 'wb') as fp:
        for x in buf:
            data = int(x, 16)
            fp.write(chr(data))

if __name__ == '__main__':
    filename = '/root/tmp/test.txt'
    retlist = readfile(filename)
    filewrite(retlist)