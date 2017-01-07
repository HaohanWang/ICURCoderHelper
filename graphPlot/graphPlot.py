__author__ = 'Haohan Wang'

from utility.filePath import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def getNames():
    text = open(folderPath+'allUnion.txt').read().splitlines()
    names = []
    for line in text[1:]:
        items = line.split('\t')
        names.append(items[0])
    return names

def drawGraph():
    names = getNames()
    # text = np.loadtxt(folderPath+'allUnion_graphWeights.csv', delimiter=',', skiprows=1)
    graph = np.genfromtxt(folderPath+'allUnion_graphWeights.csv', delimiter=',')[1:,1:]
    # graph = text[:, 1:]
    print graph.shape
    print len(names)
    assert graph.shape[0] == len(names)
    inds = np.where(graph!=0)
    print inds

if __name__ == '__main__':
    drawGraph()