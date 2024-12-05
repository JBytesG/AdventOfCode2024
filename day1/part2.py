import numpy as np

map = {}
list1 = []
sum = 0
f = open("input", "r")

for l in f:
    nums = l.strip("\n").split("   ")
    list1.append(nums[1])

    if map.get(nums[0]) is None:
        map[nums[0]] = 1
    else:
        map[nums[0]] += 1

for i in list1:
    if map.get(i) is not None:
        sum += map[i] * int(i)

print(sum)
