__author__ = 'Haohan Wang'

from utility.filePath import *
import numpy as np

from matplotlib import pyplot as plt

def organizeResults(fileCategory='healthy', sparse=True):
    if fileCategory == 'healthy':
        graphPath = healthyGraphPath
    else:
        graphPath = diseasedGraphPath
    if sparse:
        tail = 'sparse'
    else:
        tail = 'dense'

    files = ['union_metab_stool']

    data = None

    for filename in files:
        for i in range(1, 101):
            try:
                text = [line.strip() for line in open(graphPath+filename+'.csv_'+str(i)+'_'+tail)]
            except:
                text = None

            if i == 1:
                data = np.zeros([len(text), len(text)])

            if text is not None:
                for line in text:
                    items = line.split()
                    if items[1].startswith('integer'):
                        pass
                    elif items[1].startswith('c('):
                        nums = items[1][2:-1].split(',')
                        s = int(items[0])
                        for t in nums:
                            data[s-1, int(t)-1] += 1
        data = data/20.0
        # print np.max(data)
        data[data<=0.75] = 0
        data[data>0.75] = 1
        # print np.where(data==1)

        # plt.imshow(data)
        # plt.show()

        np.savetxt(graphPath+filename+'_'+tail+'_bootstrap.csv', data, delimiter=',')

if __name__ == '__main__':
    sparse=False
    organizeResults('healthy', sparse=sparse)
    organizeResults('diseased', sparse=sparse)
