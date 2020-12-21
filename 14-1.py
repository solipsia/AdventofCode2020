rawdata = open("14-1.input.txt").readlines()
data={}
maskstr=""
for item in rawdata:
    if item[0:4]=="mask":
        maskstr=item[6:].strip()
        mask0=0
        mask1=0
        for i,c in enumerate(maskstr[::-1]):
            if c=="1":
                mask1+=2**(i)
            if c=="0":
                mask0+=2**(i)
        mask0=mask0 ^ (2**36-1)
    if item[0:3]=="mem":
        adr=int(item[item.find("[")+len("["):item.rfind("]")])
        dat=int(item[item.find("= ")+len("= "):].strip())
        if adr not in data:
            data[adr]=0
        data[adr]=(dat | mask1) & mask0

sum=0
for i in data:
    sum+=data[i]
print(sum)
