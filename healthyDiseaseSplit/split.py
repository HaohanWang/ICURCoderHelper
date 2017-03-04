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
    text = open(transposedPath+filename).read().splitlines()

    f1 = open(healthyDataPath+filename, 'w')
    f2 = open(diseasedDataPath+filename, 'w')
    f1.writelines(text[0]+'\n')
    f2.writelines(text[0]+'\n')
    for line in text[1:]:
        items = line.split('\t')
        if items[0] in healthPeople:
            f1.writelines(line+'\n')
        if items[0] in diseasedPeople:
            f2.writelines(line+'\n')
    f1.close()
    f2.close()

if __name__ == '__main__':
    h, d = getPhenos()
    split('union_rna_metab.txt', h, d)
    split('union_metab_stool.txt', h, d)
    split('union_rna_stool.txt', h, d)