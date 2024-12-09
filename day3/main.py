import re

f = open("input", "r")
sum = 0

for l in f:
    line = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", l)
    for mul in line:
        mul = mul.strip("mul(")
        mul = mul.strip(")")
        nums = mul.split(",")
        sum += int(nums[0]) * int(nums[1])

print(sum)
