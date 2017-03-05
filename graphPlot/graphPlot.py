__author__ = 'Haohan Wang'

from utility.filePath import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

from analyzeResult.analyzeResults import cleanName

def pickColor(i):
    colorsListMap = [2000, 757, 28] # rnaSeq, plasma, stool
    if i < colorsListMap[0]:
        return 0.0
    if i < colorsListMap[0] + colorsListMap[1]:
        return 0.5
    else:
        return 1.0

def generateColorDictionary():
    rnames = cleanNames([line.strip() for line in open(mergePath+'rna_seq_nameList.txt')])
    snames = cleanNames([line.strip() for line in open(mergePath+'stool_micro_nameList.txt')])
    pnames = cleanNames([line.strip() for line in open(mergePath+'plasma_metab_nameList.txt')])

    colorDict = {}
    for a in rnames:
        colorDict[a] = 0.0
    for b in snames:
        colorDict[b] = 0.5
    for c in pnames:
        colorDict[c] = 1.0
    return colorDict

def drawGraph(colorDict):
    G = nx.DiGraph()

    # healthy ones
    for r, d, f in os.walk(healthyResultPath):
        for fn in f:
            edges = []
            text = [line.strip() for line in open(healthyResultPath+fn)]
            if len(text)>0 and len(text)<1000:
                for line in text:
                    items = line.split(',')
                    nodeA = items[0]
                    nodeB = items[1]
                    edges.append((nodeA, nodeB))
                G.add_edges_from(edges)
                values = [colorDict.get(node, 0.25) for node in G.nodes()]

                pos = nx.spring_layout(G)
                nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = values)
                nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', arrows=True)
                plt.savefig(healthyFigurePath+fn.split('.')[0]+'.pdf', format='pdf')
                plt.clf()

    # diseased ones
    for r, d, f in os.walk(diseasedResultPath):
        for fn in f:
            edges = []
            text = [line.strip() for line in open(diseasedResultPath+fn)]
            if len(text)>0 and len(text)<1000:
                for line in text:
                    items = line.split(',')
                    nodeA = items[0]
                    nodeB = items[1]
                    edges.append((nodeA, nodeB))
                G.add_edges_from(edges)
                values = [colorDict.get(node, 0.25) for node in G.nodes()]

                pos = nx.spring_layout(G)
                nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = values)
                nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', arrows=True)
                plt.savefig(diseasedFigurePath+fn.split('.')[0]+'.pdf', format='pdf')
                plt.clf()

def cleanNames(l):
    r = []
    for n in l:
        r.append(cleanName(n))
    return r

if __name__ == '__main__':
    cd = generateColorDictionary()
    drawGraph(cd)