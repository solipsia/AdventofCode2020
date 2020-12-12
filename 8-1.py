
rawdata = open("8-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))

acc=0
cp=0

timesrun = [0]*len(data)
looping=0
while not looping:
    ins = data[cp][0:3]
    val = int(data[cp][4:])
    print(ins,val,acc,cp,looping)
    timesrun[cp]=1
    if ins=='nop':
        cp=cp+1
    if ins=='acc':
        acc=acc+val
        cp=cp+1
    if ins=='jmp':
        cp=cp+val
    if timesrun[cp]==1:
        looping=1
        print(acc)


