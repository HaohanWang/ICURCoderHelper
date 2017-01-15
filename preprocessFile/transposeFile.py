__author__ = 'Haohan Wang'

from utility.filePath import *

def transposeFile(filename):
    # text = [line.strip() for line in open(folderPath+filename)]
    text = open(folderPath+filename).read().splitlines()
    data = []
    dim = 0
    for line in text:
        line = line.strip()
        items = line.split('\t')
        print dim
        dim = len(items)
        data.append(items)
    f = open(folderPath+filename[:-4]+'_transposed.txt', 'w')
    for j in range(dim):
        tmp = []
        for i in range(len(data)):
            tmp.append(data[i][j])
        f.writelines('\t'.join(tmp)+'\n')
    f.close()


if __name__ == '__main__':
    transposeFile('union_metab_stool.txt')
    transposeFile('union_rna_metab.txt')
    transposeFile('union_rna_stool.txt')