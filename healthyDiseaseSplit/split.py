__author__ = 'Haohan Wang'

from utility.filePath import *

def getPhenos():
    diseased = []
    health = []
    phenoText = open(originPath+'phenos.txt').read().splitlines()
    for line in phenoText[1:]:
        items = line.split('\t')
        pid = items[0]
        did = items[11]
        if did.strip() != '':
            if int(did) == 0:
                health.append(pid) # todo: check here: whether the healthy and diseased are correct
            else:
                diseased.append(pid)
    return health, diseased



def split(filename, healthPeople, diseasedPeople):
    text = open(mergePath+filename).read().splitlines()
    ids = text[0].split('\t')
    hind = []
    dind = []
    for i in range(len(ids)):
        if ids[i] in healthPeople:
            hind.append(i)
        elif ids[i] in diseasedPeople:
            dind.append(i)

    f1 = open(healthyDataPath+filename, 'w')
    f2 = open(diseasedDataPath+filename, 'w')
    for line in text:
        items = line.split('\t')
        f1.writelines(items[0])
        f2.writelines(items[0])
        for i in range(len(items)):
            if i in hind:
                f1.writelines('\t'+items[i])
            if i in dind:
                f2.writelines('\t'+items[i])
        f1.writelines('\n')
        f2.writelines('\n')
    f1.close()
    f2.close()

if __name__ == '__main__':
    h, d = getPhenos()
    split('union_rna_metab.txt', h, d)
    split('union_metab_stool.txt', h, d)
    split('union_rna_stool.txt', h, d)