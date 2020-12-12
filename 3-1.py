
rawdata = open("3-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))
   
treehits=0
x=0
for line in data:
    print(len(line),x,line[x%(len(line)-1)],line)
    if line[x%(len(line)-1)]=='#':
        treehits=treehits+1
    x=x+3

    
print(treehits) 