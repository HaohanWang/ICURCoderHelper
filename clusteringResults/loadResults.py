__author__ = 'Haohan Wang'

import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

from scipy.stats import pearsonr

from utility.filePath import *


def loadStoolMicrobeResults():
    text = [line.strip() for line in open(normalizedPath+'stool_micro.txt')]

    data = []
    ids = []
    for i in range(len(text)):
        if i == 0:
            ids_raw = text[i].split('\t')[1:]
            for m in ids_raw:
                e = m.find('S')
                ids.append(int(m[1:e]))
        else:
            items = text[i].split('\t')[1:]
            line = [float(item) for item in items]
            data.append(line)
    data = np.array(data)
    data = data.T

    return data, ids

def loadMetabResults():
    text = [line.strip() for line in open(normalizedPath+'plasma_metab.txt')]

    data = []
    ids = []
    for i in range(len(text)):
        if i == 0:
            ids_raw = text[i].split('\t')[1:]
            for m in ids_raw:
                ids.append(int(m))
        else:
            items = text[i].split('\t')[1:]
            line = [float(item) for item in items]
            data.append(line)
    data = np.array(data)
    data = data.T

    return data, ids


def cleanPhenotype(users):
    phenoText = open(originPath+'phenos.txt').read().splitlines()
    deaths = {}
    ids = []
    for line in phenoText[1:]:
        items = line.split('\t')
        id = int(items[0])
        try:
            deaths[id] = float(items[15])
        except:
            ids.append(id)
            # deaths[id] = 0 # missing deaths, set to zero
    ds = [deaths[uid] for uid in deaths]
    mv = np.mean(ds)
    for mid in ids:
        deaths[mid] = mv
    ds = [deaths[uid] for uid in users]
    return ds

def clusteringAnalysis():
    '''
    this is the wrong one that works on clusters of subjects
    :return:
    '''
    data, ids = loadStoolMicrobeResults()
    # data, ids = loadMetabResults()
    phenos = cleanPhenotype(ids)

    km = KMeans(n_clusters=2, init='k-means++')
    km.fit(data)

    labels = km.labels_

    # for i in range(len(labels)):
    #     print labels[i], phenos[i]
    # plt.scatter(labels, phenos)
    # plt.title('Metab')
    # plt.xlabel('cluster label')
    # plt.ylabel('phenotype')
    # plt.show()

    print pearsonr(labels, phenos)

if __name__ == '__main__':
    clusteringAnalysis()