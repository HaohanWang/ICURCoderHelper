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

def pickColor(i):
    colorsListMap = [2000, 757, 28] # rnaSeq, plasma, stool
    if i < colorsListMap[0]:
        return 0.0
    if i < colorsListMap[0] + colorsListMap[1]:
        return 0.5
    else:
        return 1.0

def drawGraph():
    G = nx.DiGraph()
    edges = []
    valueMap = {}
    names = getNames()
    # text = np.loadtxt(folderPath+'allUnion_graphWeights.csv', delimiter=',', skiprows=1)
    graph = np.genfromtxt(folderPath+'allUnion_graphWeights.csv', delimiter=',')[1:,1:]
    # graph = text[:, 1:]
    assert graph.shape[0] == len(names)
    inds = np.where(graph!=0)
    x = inds[0]
    y = inds[1]
    for i in range(len(x)):
        xi = x[i]
        yi = y[i]
        weights = graph[xi, yi]
        nodeA = names[xi]
        nodeB = names[yi]
        if nodeA not in valueMap:
            valueMap[nodeA] = pickColor(xi)
        if nodeB not in valueMap:
            valueMap[nodeB] = pickColor(yi)
        edges.append((nodeA, nodeB))
    G.add_edges_from(edges)
    values = [valueMap.get(node, 0.25) for node in G.nodes()]

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = values)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', arrows=True)
    plt.show()

def cleanNames(names):
    result = []
    for n in names:
        tmp = n.replace('"', '')
        tmp = tmp.replace('\\', '')
        tmp = tmp.replace('*', '')
        tmp = tmp.replace(',', '_')
        result.append(tmp)
    return result

def writeAdjacentMatrix():
    names = getNames()
    names = cleanNames(names)
    graph = np.genfromtxt(folderPath+'allUnion_graphWeights.csv', delimiter=',')[1:,1:]
    assert graph.shape[0] == len(names)
    inds = np.where(graph!=0)
    x = inds[0]
    y = inds[1]
    f = open(folderPath+'allUnion_adjacentWeights.csv', 'w')
    for i in range(len(x)):
        xi = x[i]
        yi = y[i]
        weight = graph[xi, yi]
        nodeA = names[xi]
        nodeB = names[yi]
        f.writelines(nodeA+','+nodeB+','+str(weight) + '\n')
    f.close()


if __name__ == '__main__':
    writeAdjacentMatrix()