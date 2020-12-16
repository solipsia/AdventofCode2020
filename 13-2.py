##from math import gcd
#rawdata = open("13-1.input.txt").readlines()
#schedule=rawdata[1].split(',')

##/*
##        ** Previous bus is 7, this bus is 13, with delay +1.
##        ** A time T is needed such that:
##        **      7x == T
##        **     13y == (T + 1)
##        **
##        ** Performing an iterative search for T on multiples of 7 and checking (T + 1)
##        ** eventually reveals that:
##        **   (7 * 11) == 77
##        **   (13 * 6) == 78
##        **
##        ** To find further times that match this condition, imagine some value W added to T.
##        **    7j == T + W
##        **   13k == (T + 1) + W
##        ** Substituting:
##            **    7j == 7x + W,  and j == x + (W / 7)
##            **   13k == 13y + W, and k == y + (W / 13)
##            ** For j and k to be integers, since x and y are integers, W must be a multiple of both 7 and 13.
##            ** Since all input numbers are conveniently prime, the smallest multiple of both 7 and 13 is (7 * 13).
##            ** Thus, W == (7 * 13) == 91.
##            **
##            **
##            ** Next, a time T is needed such that:
##            **      7x == T
##            **     13y == (T + 1)
##            **     59z == (T + 4)
##            **
##            ** Performing an iterative search from 77, adding multiples of 91, eventually reveals that:
##            **    (7 * 50) == 350
##            **   (13 * 27) == 351
##            **    (59 * 6) == 354
##            **
##            ** As above, the next T that matches this condition would be 350 + (7 * 13 * 59) == 350 + (5369) == 5719.

#buses=[]
#ofs=[]
#solution=0
#for num,bus in enumerate(schedule):
#    if bus!='x':
#        buses.append(int(bus))
#        ofs.append(num)

#print(buses)
#print(ofs)
#multiple=buses[0]
#t=0
#for span in range(1,len(buses)):
#    print('span',span)
#    done=0
#    t=solution
#    while not done:
#        t=t+multiple
#        tally=(t//buses[span]+1)*buses[span]
#        if tally==t+ofs[span]:
#            solution=tally-ofs[span]
#            done=1
#            print('span,multiple,i,bus,solution:',span,multiple,span,buses[span],solution)
#            multiple=multiple*buses[span]
#print(solution)
##for span in range(1,len(buses)):
##    #print('span',span)
##    valid=0
##    done=0
##    t=solution
##    while not done:
##        t=t+multiple
##        i=span
##        tally=0
##        while tally<t:
##            tally=tally+buses[i]
##        if tally==t+ofs[i]:
##            solution=tally-ofs[i]
##            if i==span:
##                done=1
##                print('span,multiple,i,bus,solution:',span,multiple,i,buses[i],solution)
##                multiple=multiple*buses[i]

##for span in range(1,len(buses)):
##    #print('span',span)
##    valid=0
##    done=0
##    t=solution
##    while not done:
##        t=t+multiple
##        for i in range(span+1):
##            tally=0
##            while tally<t:
##                tally=tally+buses[i]
##            if tally==t+ofs[i]:
##                solution=tally-ofs[i]
##                if i==span:
##                    done=1
##                    print('solution:',solution)
##                    multiple=multiple*buses[i]
##            else:
##                break

with open("13-1.input.txt") as F:
    F.readline() # ignore the first line of the input
    buses = F.readline().strip().split(',')

# create pairs of (divisor, remainder) for every available bus
buses = [(int(buses[i]), (int(buses[i]) - i) % int(buses[i]))
    for i in range(len(buses)) if buses[i] != 'x']

result = 0
increment = 1

for bus in buses:
    while result % bus[0] != bus[1]:
        result += increment
    increment *= bus[0]

print(result)