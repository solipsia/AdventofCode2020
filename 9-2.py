
rawdata = open("9-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append(int(item))

prelen=25

for cp in range(prelen,len(data)):
    test=int(data[cp])
    preamble=[int(i) for i in data[cp-prelen:cp]]
    valid=0
    for num1 in preamble:
        for num2 in preamble:
            if num1!=num2 and num1+num2==test:
                valid=1
    
    if valid==0:
        for cpstart in range(len(data)):
            for cpend in range(cpstart+1,len(data)):
                sum=0
                smallest=999999999999999
                largest=-1
                for num in data[cpstart:cpend]:
                    smallest=min(smallest,(num))
                    largest=max(largest,(num))
                    sum=sum+(num)
                    if sum==test:
                        print(smallest+largest)
                        quit()