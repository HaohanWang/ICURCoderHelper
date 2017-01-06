__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np
import operator

def featureSelection(filename, fn=2000):
    text = open(folderPath+filename).read().splitlines()
    data = []
    for line in text:
        line = line.strip()
        items = line.split('\t')
        data.append(items)

    users = data[0][1:]
    geneIDs = []
    values = []
    for i in range(1, len(data)):
        geneIDs.append(data[i][0])
        values.append([float(k) for k in data[i][1:]])

    phenoText = open(folderPath+'phenos.txt').read().splitlines()
    deaths = {}
    ids = []
    for line in phenoText[1:]:
        items = line.split('\t')
        id = items[0]
        try:
            deaths[id] = float(items[15])
        except:
            print 'here'
            ids.append(id)
            # deaths[id] = 0 # missing deaths, set to zero
    ds = [deaths[uid] for uid in users]
    mv = np.mean(ds)
    for mid in ids:
        deaths[mid] = mv
    ds = [deaths[uid] for uid in users]

    corr = {}
    for i in range(len(values)):
        cor = np.corrcoef(values[i], ds)[0, 1]
        corr[i] = cor

    sc = sorted(corr.items(), key=operator.itemgetter(1))
    sc.reverse()
    print sc
    valueNew = []
    geneIDNew = []
    for i in range(fn):
        valueNew.append(values[sc[i][0]])
        geneIDNew.append(geneIDs[sc[i][0]])

    f = open(folderPath+filename[:-4]+'_selected.txt', 'w')
    f.writelines('ID:\t'+'\t'.join(users)+'\n')
    for i in range(fn):
        f.writelines(geneIDNew[i]+'\t')
        m = [str(k) for k in valueNew[i]]
        f.writelines('\t'.join(m)+'\n')
    f.close()

if __name__ == '__main__':
    featureSelection('rna_seq.txt')