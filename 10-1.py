
rawdata = open("10-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append(int(item))

data.append(0)
data.append(max(data)+3)
data.sort()
one=0
three=0
for a in range(0,len(data)-1):
    if data[a+1]-data[a]==3:
        three=three+1
    if data[a+1]-data[a]==1:
        one=one+1

print(one*three)


