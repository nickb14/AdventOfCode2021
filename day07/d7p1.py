import statistics

def main():

    with open("/workspace/AdventOfCode2021/day7/input.txt") as f:
        crabs = f.read().split(',')
    crabs = list(map(int, crabs))

    fuel = calcFuel(crabs, int(statistics.median(crabs)))
    print(fuel)

def calcFuel(crabs, m): #I think the median is always best because math...
    fuel = 0
    for c in crabs:
        fuel += abs(c-m)
    return fuel

main()