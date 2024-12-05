
f = open("input", "r")
sum = 0

for l in f:
    line = l.strip("\n").split(" ")
    decrFlag = False
    incrFlag = False
    badFlag = False

    for i in range(len(line) - 1):
        diff = int(line[i]) - int(line[i+1])

        if diff >= 1 and diff <= 3:
            if not (decrFlag or incrFlag):
                decrFlag = True
            elif not decrFlag:
                badFlag = True
                break
        elif diff <= -1 and diff >= -3:
            if not (decrFlag or incrFlag):
                incrFlag = True
            elif not incrFlag:
                badFlag = True
                break
        else:
            badFlag = True
            break
    
    if not badFlag:
        sum += 1

print(sum)