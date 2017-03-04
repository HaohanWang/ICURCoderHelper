__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

import os

def generateNameList():
    nameListMapping = {}
    text = [line.strip() for line in open(mergePath+'rna_seq_nameList.txt')]
    for i in range(len(text)):
        nameListMapping['r'+str(i)] = text[i]

    text = [line.strip() for line in open(mergePath+'stool_micro_nameList.txt')]
    for i in range(len(text)):
        nameListMapping['s'+str(i)] = text[i]

    text = [line.strip() for line in open(mergePath+'plasma_metab_nameList.txt')]
    for i in range(len(text)):
        nameListMapping['p'+str(i)] = text[i]
    return nameListMapping

def generateNameRules(filename):
    if filename.startswith('union_metab_stool'):
        return 693, 'p', 's'
    elif filename.startswith('union_rna_metab'):
        return 200, 'r', 'p'
    else:
        return 200, 'r', 's'

def matchName(filename, x, y, nameListMapping):
    t, a, b = generateNameRules(filename)
    if x < t:
        xname = nameListMapping[a+str(x)]
    else:
        xname = nameListMapping[b+str(x-t)]
    if y < t:
        yname = nameListMapping[a+str(y)]
    else:
        yname = nameListMapping[b+str(y-t)]
    return xname, yname

def writeOutResults(nameListMapping):
    # healthy ones
    for r, d, f in os.walk(healthyGraphPath):
        for fn in f:
            data = []
            text = [line.strip() for line in open(healthyGraphPath+fn)]
            for line in text[1:]:
                d = []
                items = line.split(',')
                for item in items[1:]:
                    d.append(float(item))
                data.append(d)
            data = np.array(data)
            ind1, ind2 = np.where(data!=0)
            f = open(healthyResultPath+fn.split('.')[0]+'_'+fn.split('_')[-1]+'.txt', 'w')

            for i in range(ind1.shape[0]):
                x = ind1[i]
                y = ind2[i]
                xname, yname = matchName(fn, x, y, nameListMapping)
                f.writelines(xname+'\t'+yname+'\t'+str(data[x, y])+'\n')
            f.close()

    # diseased Ones
    for r, d, f in os.walk(diseasedGraphPath):
        for fn in f:
            data = []
            text = [line.strip() for line in open(diseasedGraphPath+fn)]
            for line in text[1:]:
                d = []
                items = line.split(',')
                for item in items[1:]:
                    d.append(float(item))
                data.append(d)
            data = np.array(data)
            ind1, ind2 = np.where(data!=0)
            f = open(diseasedResultPath+fn.split('.')[0]+'_'+fn.split('_')[-1]+'.txt', 'w')

            for i in range(ind1.shape[0]):
                x = ind1[i]
                y = ind2[i]
                xname, yname = matchName(fn, x, y, nameListMapping)
                f.writelines(xname+'\t'+yname+'\t'+str(data[x, y])+'\n')
            f.close()


if __name__ == '__main__':
    nameListMapping = generateNameList()
    writeOutResults(nameListMapping)