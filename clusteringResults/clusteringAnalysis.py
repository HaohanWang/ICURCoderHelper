__author__ = 'Haohan Wang'

from sklearn.cluster import KMeans

from loadResults import loadStoolMicrobeResults, loadMetabResults, cleanPhenotype

def clusterResults():
    # data, ids = loadStoolMicrobeResults()
    data, ids = loadMetabResults()
    phenos = cleanPhenotype(ids)

    km = KMeans(n_clusters=2, init='k-means++')
    km.fit(data.T)

    labels = km.labels_

    for i in labels:
        print i


if __name__ == '__main__':
    clusterResults()

