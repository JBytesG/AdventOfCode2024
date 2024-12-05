
f = open("input", "r")
sum = 0

for l in f:
    line = l.strip("\n").split(" ")
    decrFlag = False
    incrFlag = False
    badFlag = 0

    for i in range(len(line) - 1):
        diff = int(line[i]) - int(line[i+1])

        if diff >= 1 and diff <= 3:
            if not (decrFlag or incrFlag):
                decrFlag = True
            elif not decrFlag:
                badFlag +=1
        elif diff <= -1 and diff >= -3:
            if not (decrFlag or incrFlag):
                incrFlag = True
            elif not incrFlag:
                badFlag += 1
        else:
            badFlag += 1
        
        if badFlag > 1:
            break
    
    if not badFlag > 1:
        sum += 1
        print(l)

print(sum)