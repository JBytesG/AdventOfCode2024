import re

f = open("input", "r")
sum = 0
do = True

for l in f:
    line = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", l)
    
    for func in line:

        if func[0] == 'm' and do:
            func = func.strip("mul(")
            func = func.strip(")")
            nums = func.split(",")
            sum += int(nums[0]) * int(nums[1])
        if func[2] == 'n':
            do = False
        if func[2] == '(':
            do = True


print(sum)
