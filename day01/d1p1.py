nums = []

with open("day01/input.txt") as f:
    line = f.readline()
    while line:
        nums.append(int(line))
        line = f.readline()

tot = -1
prev = 0 #just start with this because total starts at -1 (supposed to ignore first value)
for num in nums:
    if num > prev:
        tot += 1
    prev = num

print(tot)