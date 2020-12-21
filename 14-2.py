import itertools
rawdata = open("14-1.input.txt").readlines()

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def dec(s):
    result=0
    for i,c in enumerate(s[::-1]):
            if c=="1":
                result+=2**(i)
    return result


data={}
maskstr=""
for item in rawdata:
    if item[0:4]=="mask":
        maskstr=item[6:].strip()

    if item[0:3]=="mem":
        adr=int(item[item.find("[")+len("["):item.rfind("]")])
        dat=int(item[item.find("= ")+len("= "):].strip())

        adrstr = bin(adr).rjust(36,"0")
        adrlist = list(adrstr)
        Xs = 0
        Xpos = []
        for i,x in enumerate(maskstr):
            if x=="X":
                adrlist[i]="X"
                Xs+=1
                Xpos.append(i)
            if x=="1":
                adrlist[i]="1"
        result="".join(adrlist)
        variations = [list(i) for i in itertools.product([0, 1], repeat=Xs)]

        for variation in variations:
            currentmem=list(result)
            for i,bit in enumerate(variation):
                if bit==0:
                    currentmem[Xpos[i]]="0"
                else:
                    currentmem[Xpos[i]]="1"
            newadr="".join(currentmem)
            if newadr not in data:
                data[newadr]=0
            data[newadr]=dat

sum=0
for i in data:
    sum+=data[i]
print(sum)

