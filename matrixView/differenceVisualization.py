__author__ = 'Haohan Wang'

import numpy as np
from matplotlib import pyplot as plt

from utility.filePath import *
from analyzeResult.analyzeResults import matchName, generateNameList

def differenceVisualization(nameListMapping, category='all'):
    healthGraphs = ['union_metab_stool_dense_bootstrap.csv']
    diseasedGraphs = ['union_metab_stool_dense_bootstrap.csv']

    # healthGraphs = ['union_metab_stool.csv_13', 'union_rna_metab.csv_19', 'union_rna_stool.csv_14']
    # diseasedGraphs = ['union_metab_stool.csv_14', 'union_rna_metab.csv_13', 'union_rna_stool.csv_19']

    result = ['union_metab_stool']

    plt.figure(figsize=(100,100), dpi=100)

    for c in range(len(result)):
        hfn = healthGraphs[c]
        dfn = diseasedGraphs[c]

        hdata = []
        text = [line.strip() for line in open(healthyGraphPath+hfn)]
        for line in text[1:]:
            d = []
            items = line.split(',')
            for item in items[1:]:
                if item != 'NA':
                    d.append(float(item))
                else:
                    d.append(0)
            hdata.append(d)
        hdata = np.array(hdata)
        hdata[hdata!=0] = 1
        print hdata.shape

        ddata = []
        text = [line.strip() for line in open(diseasedGraphPath+dfn)]
        for line in text[1:]:
            d = []
            items = line.split(',')
            for item in items[1:]:
                if item != 'NA':
                    d.append(float(item))
                else:
                    d.append(0)
            ddata.append(d)
        ddata = np.array(ddata)
        ddata[ddata!=0] = 1
        print ddata.shape

        diff = hdata - ddata
        print diff.shape

        if category == 'all':
            ind1, ind2 = np.where(diff!=0)

            idx1 = np.array(sorted(list(set(ind1))))
            idx2 = np.array(sorted(list(set(ind2))))

            diff = diff[idx1, :]
            diff = diff[:, idx2]

            print diff.shape
        elif category == 'from':
            count1 = np.sum(np.abs(diff), 1)
            idx1 = np.argsort(count1)[-10:]
            diff = diff[idx1,:]
            ind2 = np.where(diff!=0)[1]
            idx2 = np.array(sorted(list(set(ind2))))
            diff = diff[:, idx2]

            print diff.shape
        else:
            count2 = np.sum(np.abs(diff), 0)
            idx2 = np.argsort(count2)[-10:]
            diff = diff[:, idx2]
            ind1 = np.where(diff!=0)[0]
            idx1 = np.array(sorted(list(set(ind1))))
            diff = diff[idx1, :]

            print diff.shape

        ylabel = []
        xlabel = []

        for j in range(idx1.shape[0]):
            y = idx1[j]
            x = idx1[j]
            yname, xname = matchName(result[c], y, x, nameListMapping)
            ylabel.append(yname)

        for j in range(idx2.shape[0]):
            y = idx2[j]
            x = idx2[j]
            yname, xname = matchName(result[c], y, x, nameListMapping)
            xlabel.append(xname)

        plt.imshow(diff)
        if category == 'to':
            plt.xticks(xrange(diff.shape[1]), xlabel, rotation='vertical', fontsize=30)
            plt.yticks(xrange(diff.shape[0]), ylabel, fontsize=30)
        else:
            plt.xticks(xrange(diff.shape[1]), xlabel, rotation='vertical', fontsize=1)
            plt.yticks(xrange(diff.shape[0]), ylabel, fontsize=1)
        plt.savefig(differenceFigurePath+result[c]+'.pdf', format='pdf')


if __name__ == '__main__':
    nameListMapping = generateNameList()
    differenceVisualization(nameListMapping, category='all')