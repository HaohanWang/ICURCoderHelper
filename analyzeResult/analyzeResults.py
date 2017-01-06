__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

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


if __name__ == '__main__':
    writeOutResults()
