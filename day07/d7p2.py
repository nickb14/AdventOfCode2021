import statistics

def main():

    with open("/workspace/AdventOfCode2021/day7/input.txt") as f:
        crabs = f.read().split(',')
    crabs = list(map(int, crabs))

    fuel = calcFuel(crabs, int(statistics.mean(crabs))) #mean...
    print(int(fuel)) #well ok I don't know why but but the mean works

def calcFuel(crabs, m): #is the mean always the best for this case?
    fuel = 0
    for c in crabs:
        d = abs(c-m)
        fuel += d * (d+1) / 2 #triangle numbers!
    return fuel

main()