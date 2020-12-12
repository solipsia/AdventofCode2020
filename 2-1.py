
rawdata = open("2-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))
   
validtotal=0
for line in data:
    chartotest=line.split(' ')[1][0]
    lowerlimit=(line.split(' ')[0]).split('-')[0]
    upperlimit=(line.split(' ')[0]).split('-')[1]
    password=line.split(' ')[2]
    #print(lowerlimit,upperlimit,chartotest,password)
    counter=0
    for char in password:
        if char==chartotest:
            counter=counter+1
    if counter<=int(upperlimit) and counter>=int(lowerlimit):
        validtotal=validtotal+1
print(validtotal)