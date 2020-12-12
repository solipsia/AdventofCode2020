
rawdata = open("9-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))

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
        print(test)
        quit()