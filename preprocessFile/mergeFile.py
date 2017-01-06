__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

def cleanID(ids, fileName):
    if fileName.startswith('rna'):
        result = [int(i) for i in ids]
        return result
    if fileName.startswith('plasma'):
        result = [int(i[1:-1]) for i in ids]
        return result
    if fileName.startswith('stool'):
        result = []
        for i in ids:
            p = i.find('S')
            result.append(int(i[1:p]))
        return result

def loadIDData(fileName):
    text = open(folderPath+fileName).read().splitlines()
    ids = text[0].strip().split('\t')[1:]
    ids = cleanID(ids, fileName)
    data = [[] for i in range(len(ids))]
    for line in text[1:]:
        line = line.strip()
        items = line.split('\t')[1:]
        assert len(items) == len(ids)
        for i in range(len(items)):
            data[i].append(float(items[i]))
    result = {}
    for i in range(len(ids)):
        result[ids[i]] = data[i]

    data = np.array(data)
    result[0] = np.mean(data, 0)

    return result

def union(a, b):
    c = a + b
    return list(set(c))

def intersect(a, b):
    r = []
    for i in a:
        if i in b:
            r.append(i)
    return r

def showCommonID(rID, pID, sID):
    tmp = intersect(rID, pID)
    return intersect(tmp, sID)

def showAllID(rID, pID, sID):
    tmp = union(rID, pID)
    return union(tmp, sID)


def mergeFile():
    fileName1 = 'rna_seq_selected.txt'
    fileName2 = 'plasma_metab.txt'
    fileName3 = 'stool_micro.txt'

    r = loadIDData(fileName1)
    p = loadIDData(fileName2)
    s = loadIDData(fileName3)

    rID = [i for i in r]
    pID = [i for i in p]
    sID = [i for i in s]

    print rID
    print pID
    print sID

    print intersect(rID, pID)
    print intersect(pID, sID)
    print intersect(rID, sID)

    c = showCommonID(rID, pID, sID)
    print len(c)
    print c

    print '-----------'

    print union(rID, pID)
    print union(pID, sID)
    print union(rID, sID)

    a = showAllID(rID, pID, sID)
    print len(a)
    print a

if __name__ == '__main__':
    mergeFile()