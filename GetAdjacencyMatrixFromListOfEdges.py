#!/usr/bin/python
import csv
from collections import OrderedDict
import sys
from collections import defaultdict
import numpy as np

idsAll=[]
idsRows=[]
d=OrderedDict()
path1="/home/anto/CitationNetworkBinary.txt"
with open(path1,"rb") as f:
    reader=csv.reader(f)
    for line in reader: 
        #idsRows.append(line[0])
        for ll in line:
            if ll not in idsAll:
                idsAll.append(ll)
        d[line[0]]=line[1:]
f.close()
#keep only the unique ids to built the adjacency matrix
idsUnique=set(idsAll)
idsRows=list(idsUnique)
adjMatrix=np.zeros(shape=(len(idsRows)+1,len(idsRows)+1))
adjMatrix[1:,0]=idsRows
adjMatrix[0,1:]=idsRows

count=1

for i in idsRows:
    if i in d:
        for j in d[i][0:]:
            itemindex = np.where(adjMatrix[0,1:]==int(j)) # find in which column is the node to whom node i points/is connected
            adjMatrix[count,itemindex[0]+1]=1
    count=count+1

print adjMatrix.shape
print np.nonzero(adjMatrix)
# save adjacency in sparse matrix format kai the ids included in the final adjacency
np.savetxt("/home/anto/AdjacencyInSparse.txt", np.transpose(np.nonzero(adjMatrix[0:,0:])), delimiter=",")
np.savetxt("/home/anto/110AdjacencyIDs.txt", adjMatrix[1:,0], delimiter=",")
