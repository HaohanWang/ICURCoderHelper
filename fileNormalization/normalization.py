__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

#normalizing each term across patient

def normalization(filename):
    text = open(selectedPath+filename).read().splitlines()
    data = []
    names = []
    for line in text[1:]:
        d = []
        items = line.split('\t')
        for item in items[1:]:
            d.append(float(item))
        names.append(items[0])
        d = [m/max(d) for m in d]
        data.append(d)


    f = open(normalizedPath+filename, 'w')
    f.writelines(text[0]+'\n')
    for i in range(len(data)):
        f.writelines(names[i])
        for num in data[i]:
            f.writelines('\t'+str(num))
        f.writelines('\n')

    f.close()

if __name__ == '__main__':
    normalization('rna_seq.txt')
    normalization('plasma_metab.txt')
    normalization('stool_micro.txt')