f = open("input", "r")
map = {}
sum = 0

for l in f:
    l = l.strip("\n")
    if l.__contains__("|"):
        nums = l.split("|")
        if map.get(nums[0]) is None:
            map[nums[0]] = [nums[1]]
        else:
            map[nums[0]].append(nums[1])
    elif l.__contains__(","):
        nums = l.split(",")
        badFlag = False
        for i in range(len(nums)):
            if map.get(nums[i]):
                for rule in map[nums[i]]:
                    for j in range(i):
                        if nums[j] == rule:
                            badFlag = True
                            break
                    if badFlag:
                        break
            if badFlag:
                break
        if not badFlag:    
            sum += int(nums[int(len(nums)/2 + .5)])

print(sum)
                    
    