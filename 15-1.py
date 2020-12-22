import itertools
input=[12,1,16,3,11,0]
mem={}
turn=0
last=0
say=0
for i in itertools.cycle(input):
    last=say
    if turn<=len(input)-1:
        say=i
        mem[say]=[turn]
    else:
        if len(mem[last])==1: #last said was first time
            say=0
        else: #say diff
            say=mem[last][-1]-mem[last][-2]
        if say in mem:
            mem[say].append(turn)
        else: 
            mem[say]=[turn]
    
    if turn==2020:
        break
    turn+=1


print(last)