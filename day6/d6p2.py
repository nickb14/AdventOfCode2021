def main():

    with open("/workspace/AdventOfCode2021/day6/input.txt") as f:
        fishList = f.read().split(',')
    fishList = list(map(int, fishList))

    fish = [0] * 9
    for f in fishList:
        fish[f] += 1 #it works I guess
    
    for i in range(256): #that's pretty epic
        new = fish.pop(0)
        fish[6] += new
        fish.append(new)
    
    print(sum(fish))

main()