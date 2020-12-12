import itertools
import more_itertools
from more_itertools import flatten

rawdata = open("10-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append(int(item))

data.append(0)
data.append(max(data)+3)
data.sort()
staticindex=[0]

#find mandatory adapters, then test all combos of those inbetween them

def isvalid(seq):
    for i in range(len(seq)-1):
        if seq[i+1]-seq[i]>3:
            return 0
    return 1

for a in range(0,len(data)-2):
    if data[a+2]-data[a]>3:
        staticindex.append(a+1)
staticindex.append(len(data)-1)

batches=[]
for count,s in enumerate(staticindex[:-1]):
    if staticindex[count+1]-s>1: 
        batches.append([i for i in range(s+1,staticindex[count+1])])

totalcombos=1
for b in batches:
    seq=[]
    for i in b:
        seq.append(data[i])
    batchcombos = [list(x) for x in list(more_itertools.powerset(seq))]
    validbatchcombos=0
    for c in batchcombos:
        testset=[data[b[0]-1]]
        for i in c:
            testset.append(i)
        testset.append(data[1+b[len(b)-1]])
        if isvalid(testset):
            validbatchcombos=validbatchcombos+1
    totalcombos=totalcombos*validbatchcombos

print(totalcombos)