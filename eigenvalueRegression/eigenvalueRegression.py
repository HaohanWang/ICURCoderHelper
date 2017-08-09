__author__ = 'Haohan Wang'

import numpy as np

from utility.filePath import originPath

from sklearn.linear_model import LinearRegression


def cleanMetabData():
    text = open(originPath + 'plasma_metab.txt').read().splitlines()
    pids = []
    mat = []
    sub = {}
    for i in range(len(text)):
        line = text[i]
        if i == 0:
            items = line.split('\t')
            for j in range(2, len(items)):
                pids.append(int(items[j]))
        else:
            items = line.split('\t')
            sid = items[1]
            if sid not in sub:
                sub[sid] = [i - 1]
            else:
                sub[sid].append(i - 1)
            m = [float(items[k]) for k in range(2, len(items))]
            mat.append(m)
    mat = np.array(mat)
    mat = (mat - np.min(mat)) / (np.max(mat) - np.min(mat))

    for k in sub:
        sub[k] = np.array(sub[k])

    X = {}
    c = -1
    sids = []
    for pid in pids:
        c += 1
        x = []
        for sid in sub:
            if sub[sid].shape[0]>10:
                sids.append(sid)
                r = sub[sid]
                m = mat[r, c]
                x.append(np.dot(m.T, m))
        X[pid] = np.array(x)
    return X, sids


def cleanStoolFile():
    text = open(originPath + 'stool_micro.txt').read().splitlines()
    pids = []
    sname = []
    data = []
    for i in range(6):
        line = text[i]
        if i == 0:
            items = line.split('\t')
            for j in range(1, len(items)):
                n = items[j].find('S')
                pids.append(int(items[j][1:n]))
        else:
            items = line.split('\t')
            sname.append(items[0])
            m = [float(items[n]) for n in range(1, len(items))]
            data.append(m)
    data = np.array(data)
    data = (data - np.min(data)) / (np.max(data) - np.min(data))

    X = {}
    c = -1
    for pid in pids:
        c += 1
        X[pid] = data[:, c]

    return X, sname

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


def calculateRegressionCoefficient():
    X, sids = cleanMetabData()
    Y, sname = cleanStoolFile()
    users = [k for k in X]
    y = cleanPhenotype(users)

    # coefficient with phenotype
    data = [X[k] for k in users]
    data = np.array(data)
    print data.shape
    print '-------------------'
    lr = LinearRegression()
    lr.fit(data, y)
    c = lr.coef_
    ind = np.argsort(np.abs(c)).tolist()
    ind.reverse()
    result =[sids[k] for k in ind[:5]]
    for i in range(5):
        print i+1, result[i]
    print
    print '-------------------'

    # coefficient with stool
    exp = []
    res = []
    for k in X:
        if k in Y:
            exp.append(X[k])
            res.append(Y[k])
    exp = np.array(exp)
    res = np.array(res)

    print exp.shape

    for i in range(len(sname)):
        print '-------------------'
        print sname[i]
        lr = LinearRegression()
        lr.fit(exp, res[:, i])
        c = lr.coef_
        ind = np.argsort(np.abs(c)).tolist()
        ind.reverse()
        result =[sids[k] for k in ind[:5]]
        for i in range(5):
            print i+1, result[i]
        print


if __name__ == '__main__':
    calculateRegressionCoefficient()
