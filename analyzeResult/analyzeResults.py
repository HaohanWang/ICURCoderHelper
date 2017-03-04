__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

def calculateFileLines():
    fileName1 = 'rna_seq_selected.txt' # 2000
    fileName2 = 'plasma_metab_selected.txt' # 693
    fileName3 = 'stool_micro.txt' # 28

    text1 = open(folderPath+fileName1).read().splitlines()
    print len(text1) - 1

    text2 = open(folderPath+fileName2).read().splitlines()
    print len(text2) - 1

    text3 = open(folderPath+fileName3).read().splitlines()
    print len(text3) - 1


def writeOutResults(fileName, threshold):
    nameListMapping = {}
    text = [line.strip() for line in open(folderPath+'rna_seq_selected_nameList.txt')]
    for i in range(len(text)):
        nameListMapping['r'+str(i)] = text[i]

    text = [line.strip() for line in open(folderPath+'stool_micro_nameList.txt')]
    for i in range(len(text)):
        nameListMapping['s'+str(i)] = text[i]

    text = [line.strip() for line in open(folderPath+'plasma_metab_selected_nameList.txt')]
    for i in range(len(text)):
        nameListMapping['p'+str(i)] = text[i]

    resultFolder = folderPath + 'results/'
    graphFolder = folderPath + 'graphs/'

    for k in range(1, 15):
        data = []
        dataText = [line.strip() for line in open(graphFolder+'union_'+fileName+'_graphWeights_'+str(k))][1:]
        for line in dataText:
            items = line.split(',')
            l = [float(item) for item in items[1:]]
            data.append(l)
        data = np.array(data)
        print data.shape

        text = open(folderPath+'union_'+fileName+'.txt').read().splitlines()
        names = []
        t = len(text)-1
        for i in range(1, len(text)):
            names.append(text[i].split()[0])
        print len(names)
        f = open(resultFolder+'union_'+fileName+'directedGraph_'+str(k)+'.tsv', 'w')
        for i in range(t):
            for j in range(t):
                if data[i,j]!=0:
                    f.writelines(nameListMapping[names[i]]+'\t'+nameListMapping[names[j]]+ '\t' + str(data[i,j])+'\n')
        f.close()

def analyzeResults(fileName, threshold):
    graphFolder = folderPath + 'graphs/'

    text = open(folderPath+ 'union_'+ fileName +'_transposed.txt').read().splitlines()
    names = text[0].split()[1:]
    t = len(names)
    # for i in range(1, len(text)):
    #     names.append(text[i].split()[0])


    for i in range(1, 18):
        print '-------------------------'
        print 'Graph', i
        data = []
        dataText = [line.strip() for line in open(graphFolder+'union_'+fileName+'_graphWeights_'+str(i))][1:]
        for line in dataText:
            items = line.split(',')
            l = [float(item) for item in items[1:]]
            data.append(l)
        data = np.array(data)

        assert data.shape[0] == data.shape[1]
        assert data.shape[0] == t


        for i in range(t):
            for j in range(t):
                if data[i,j]!=0:
                    if (i <= threshold and j > threshold) or (j<=threshold and i>threshold):
                        print names[i], names[j], data[i,j]
        print '-------------------------'


if __name__ == '__main__':
    fileThreshold1 = ('rna_stool', 2000)
    fileThreshold2 = ('rna_metab', 2000)
    fileThreshold3 = ('metab_stool', 693)

    # analyzeResults(fileThreshold3[0], fileThreshold3[1])
    writeOutResults(fileThreshold3[0], fileThreshold3[1])