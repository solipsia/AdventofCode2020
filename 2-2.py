
rawdata = open("2-1.input.txt").readlines()
data = []
for item in rawdata:
    data.append((item))
   
validtotal=0
for line in data:
    chartotest=line.split(' ')[1][0]
    pos1=int((line.split(' ')[0]).split('-')[0])
    pos2=int((line.split(' ')[0]).split('-')[1])
    password=line.split(' ')[2]
    if password[pos1-1]==chartotest and password[pos2-1]!=chartotest or password[pos2-1]==chartotest and password[pos1-1]!=chartotest:
       validtotal=validtotal+1
print(validtotal)