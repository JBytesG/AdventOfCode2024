import numpy as np

def getNums(line):
    nums = line.split("   ")
    return int(nums[0]), int(nums[1])

f = open("input", "r")
list1, list2 = [], []

for l in f:
    num1, num2 = getNums(l)
    list1.append(num1)
    list2.append(num2)

list1 = np.sort(list1)
list2 = np.sort(list2)

print(sum(abs(num1-num2)))
