def main():

    with open("/workspace/AdventOfCode2021/day6/input.txt") as f:
        fish = f.read().split(',')
        fish = list(map(int, fish))
    
    for i in range(256): #am I supposed to do more logic to make this faster because I don't want to
        fish = [f-1 for f in fish]
        new = [8] * fish.count(-1)
        fish = [f if f>=0 else 6 for f in fish]
        fish.extend(new)
        print(i)
    print(len(fish))

main()