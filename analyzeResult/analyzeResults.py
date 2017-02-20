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


def writeOutResults():
    # data = np.loadtxt(folderPath+'graphWeights.csv', delimiter=',', skiprows=1)
    # data = data[:,1:]
    # print data.shape

    data = []
    dataText = [line.strip() for line in open(folderPath+'graphWeights.csv')][1:]
    for line in dataText:
        items = line.split(',')
        l = [float(item) for item in items[1:]]
        data.append(l)
    data = np.array(data)
    print data.shape

    text = open(folderPath+'rna_stool.txt').read().splitlines()
    names = []
    t = len(text)-1
    for i in range(1, len(text)):
        names.append(text[i].split()[0])
    print len(names)
    f = open(folderPath+'directedGraph.txt', 'w')
    for i in range(t):
        for j in range(t):
            if data[i,j]!=0:
                f.writelines(names[i]+'\t'+names[j]+ '\t' + str(data[i,j])+'\n')
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


    analyzeResults(fileThreshold2[0], fileThreshold2[1])
