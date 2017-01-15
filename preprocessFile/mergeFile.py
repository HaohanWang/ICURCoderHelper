__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

def cleanID(ids, fileName):
    if fileName.startswith('rna'):
        result = [int(i) for i in ids]
        return result
    if fileName.startswith('plasma'):
        result = [int(i) for i in ids]
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
    names = []
    for line in text[1:]:
        line = line.strip()
        items = line.split('\t')
        names.append(items[0])
        values = items[1:]
        assert len(values) == len(ids)
        for i in range(len(values)):
            data[i].append(float(values[i]))
    result = {}
    for i in range(len(ids)):
        result[ids[i]] = data[i]

    data = np.array(data)
    result[0] = np.mean(data, 0).tolist()

    return result, names

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

    r, rname = loadIDData(fileName1)
    p, pname = loadIDData(fileName2)
    s, sname = loadIDData(fileName3)

    rID = [i for i in r]
    pID = [i for i in p]
    sID = [i for i in s]

    ids = showAllID(rID, pID, sID)
    result = {}
    for i in ids:
        if i != 0:
            if i in r:
                rd = r[i]
            else:
                rd = r[0]
            if i in p:
                pd = p[i]
            else:
                pd = p[0]
            if i in s:
                sd = s[i]
            else:
                sd = s[0]
            result[i] = rd + pd + sd

    names = rname + pname + sname
    t = len(names)

    f = open(folderPath + 'allUnion.txt', 'w')
    f.writelines('ID:')
    for i in range(len(ids)):
        if ids[i]!= 0:
            f.writelines('\t'+str(ids[i]))
    f.writelines('\n')
    for j in range(t):
        f.writelines(names[j])
        for i in range(len(ids)):
            if ids[i]!= 0:
                f.writelines('\t' + str(result[ids[i]][j]))
        f.writelines('\n')
    f.close()

def mergeRNA_stool():
    fileName1 = 'rna_seq_selected.txt'
    fileName2 = 'stool_micro.txt'

    r, rname = loadIDData(fileName1)
    p, pname = loadIDData(fileName2)

    rID = [i for i in r]
    pID = [i for i in p]

    ids = union(rID, pID)
    result = {}
    for i in ids:
        if i != 0:
            if i in r:
                rd = r[i]
            else:
                rd = r[0]
            if i in p:
                pd = p[i]
            else:
                pd = p[0]
            result[i] = rd + pd

    names = rname + pname
    t = len(names)

    f = open(folderPath + 'union_rna_stool.txt', 'w')
    f.writelines('ID:')
    for i in range(len(ids)):
        if ids[i]!= 0:
            f.writelines('\t'+str(ids[i]))
    f.writelines('\n')
    for j in range(t):
        f.writelines(names[j])
        for i in range(len(ids)):
            if ids[i]!= 0:
                f.writelines('\t' + str(result[ids[i]][j]))
        f.writelines('\n')
    f.close()

def mergeRNA_metab():
    fileName1 = 'rna_seq_selected.txt'
    fileName2 = 'plasma_metab_selected.txt'

    r, rname = loadIDData(fileName1)
    p, pname = loadIDData(fileName2)

    rID = [i for i in r]
    pID = [i for i in p]

    ids = union(rID, pID)
    result = {}
    for i in ids:
        if i != 0:
            if i in r:
                rd = r[i]
            else:
                rd = r[0]
            if i in p:
                pd = p[i]
            else:
                pd = p[0]
            result[i] = rd + pd

    names = rname + pname
    t = len(names)

    f = open(folderPath + 'union_rna_metab.txt', 'w')
    f.writelines('ID:')
    for i in range(len(ids)):
        if ids[i]!= 0:
            f.writelines('\t'+str(ids[i]))
    f.writelines('\n')
    for j in range(t):
        f.writelines(names[j])
        for i in range(len(ids)):
            if ids[i]!= 0:
                f.writelines('\t' + str(result[ids[i]][j]))
        f.writelines('\n')
    f.close()

def mergeMetab_stool():
    fileName1 = 'plasma_metab_selected.txt'
    fileName2 = 'stool_micro.txt'

    r, rname = loadIDData(fileName1)
    p, pname = loadIDData(fileName2)

    rID = [i for i in r]
    pID = [i for i in p]

    ids = union(rID, pID)
    result = {}
    for i in ids:
        if i != 0:
            if i in r:
                rd = r[i]
            else:
                rd = r[0]
            if i in p:
                pd = p[i]
            else:
                pd = p[0]
            result[i] = rd + pd

    names = rname + pname
    t = len(names)

    f = open(folderPath + 'union_metab_stool.txt', 'w')
    f.writelines('ID:')
    for i in range(len(ids)):
        if ids[i]!= 0:
            f.writelines('\t'+str(ids[i]))
    f.writelines('\n')
    for j in range(t):
        f.writelines(names[j])
        for i in range(len(ids)):
            if ids[i]!= 0:
                f.writelines('\t' + str(result[ids[i]][j]))
        f.writelines('\n')
    f.close()

if __name__ == '__main__':
    mergeRNA_metab()
    mergeRNA_stool()
    mergeMetab_stool()