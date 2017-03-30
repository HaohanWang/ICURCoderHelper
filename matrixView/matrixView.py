__author__ = 'Haohan Wang'

import os
import numpy as np
from matplotlib import pyplot as plt

from utility.filePath import *
from analyzeResult.analyzeResults import matchName, generateNameList


def matrixVisualization(nameListMapping):
    for r, d, f in os.walk(healthyGraphPath):
        for fn in f:
            data = []
            text = [line.strip() for line in open(healthyGraphPath+fn)]
            for line in text[1:]:
                d = []
                items = line.split(',')
                for item in items[1:]:
                    if item != 'NA':
                        d.append(float(item))
                    else:
                        d.append(0)
                data.append(d)
            data = np.array(data)

            labels = []

            for i in range(data.shape[0]):
                labels.append(matchName(fn, i, i, nameListMapping)[0])

            plt.imshow(data)
            plt.xticks(xrange(data.shape[0]), labels, rotation='vertical')
            plt.yticks(xrange(data.shape[0]), labels)
            plt.savefig(healthyFigurePath+fn.split('.')[0]+'_'+fn.split('_')[-1]+'.pdf', format='pdf')

    for r, d, f in os.walk(diseasedGraphPath):
        for fn in f:
            data = []
            text = [line.strip() for line in open(diseasedGraphPath+fn)]
            for line in text[1:]:
                d = []
                items = line.split(',')
                for item in items[1:]:
                    if item != 'NA':
                        d.append(float(item))
                    else:
                        d.append(0)
                data.append(d)
            data = np.array(data)

            labels = []

            for i in range(data.shape[0]):
                labels.append(matchName(fn, i, i, nameListMapping)[0])

            plt.imshow(data)
            plt.xticks(xrange(data.shape[0]), labels, rotation='vertical')
            plt.yticks(xrange(data.shape[0]), labels)
            plt.savefig(diseasedFigurePath+fn.split('.')[0]+'_'+fn.split('_')[-1]+'.pdf', format='pdf')

if __name__ == '__main__':
    nameListMapping = generateNameList()
    matrixVisualization(nameListMapping)