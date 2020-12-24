rawdata = open("18-1.input.txt").readlines()

depth=0
def solve(sum,depth):
    ans=0
    i = 0
    op = "+"
    num=0
    while i<len(sum):
        if sum[i]=="+":
            op="+"
        elif sum[i]=="*":
            op="*"
        elif sum[i]=="(":
            sub=sum[i+1:] 
            numtoskip=0
            pairpos=0
            for y,c in enumerate(sub):
                if c=="(":
                    numtoskip+=1
                if c==")":
                    numtoskip+=-1
                    if numtoskip==-1:
                        pairpos=y
                        break

            recurse=sub[:pairpos]
            if op=="+":
                ans+=solve(recurse,depth+1)
            elif op=="*":
                ans*=solve(recurse,depth+1)
            i+=len(recurse)
        else: # num
            if sum[i]!=")":
                num=int(sum[i])
                if op=="+":
                    ans+=num
                elif op=="*":
                    ans*=num
        i+=1
    return ans

depth=0
ans=0
for line in rawdata:
    ans+=solve(line.strip().replace(" ",""),depth)
print("ans=",ans)
