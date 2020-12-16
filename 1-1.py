
rawdata = open("1-1.input.txt").readlines()
for a in rawdata:
    for b in rawdata:
        for c in rawdata:
            if a+b+c==2020:
                print(a*b*c)


