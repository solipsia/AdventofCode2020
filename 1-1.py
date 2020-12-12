
rawdata = open("1-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append(int(item))

for a in data:
    for b in data:
        for c in data:
            if a+b+c==2020:
                print(a*b*c)


