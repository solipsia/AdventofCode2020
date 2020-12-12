rawdata = open("11-1.input.txt").readlines()
seats = []
for item in rawdata:
    seats.append(item.replace('\n','')) 


changes=0
  
#while changes==0:
#    changes=1

next=[['.']*len(seats[0])]*len(seats)

for y in range(len(seats)):
    for x in range(len(seats[0])):
        print(x,y,seats[y][x])
         