rawdata = open("13-1.input.txt").readlines()
soonest=int(rawdata[0])
schedule=rawdata[1].split(',')

depart=pow(10,8)
winner=0
for bus in schedule:
    if bus!='x':
        time=0
        while time<soonest:
            time=time+int(bus)
        if time<depart:
            winner=int(bus)
            depart=time
print(winner*(depart-soonest))


