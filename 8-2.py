
rawdata = open("8-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))

for count,line in enumerate(rawdata):
    acc=0
    cp=0
    timesrun = [0]*(len(data)+1)
    
    looping=0
    while not looping:
        ins = data[cp][0:3]
        val = int(data[cp][4:])
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
        if cp==len(data):
            print('halting',acc)
            quit()

    data = []
    for item in rawdata:
        data.append((item))

    if line[0:3]=='jmp':
        data[count]=data[count].replace('jmp','nop')
    else:
        if line[0:3]=='nop':
            data[count]=data[count].replace('nop','jmp')
