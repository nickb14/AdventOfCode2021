nums = []
with open("/workspace/AdventOfCode2021/day01/input.txt") as f:
    line = f.readline()
    while line:
        nums.append(int(line))
        line = f.readline()

windows = []
for i in range(len(nums)-2):
    windows.append(nums[i] + nums[i+1] + nums[i+2])

tot = -1
prev = 0 #just start with this because total starts at -1 (supposed to ignore first value)
for num in windows: #same logic as p1, just with windows
    if num > prev:
        tot += 1
    prev = num

print(tot)