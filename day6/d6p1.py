def main():

    with open("/workspace/AdventOfCode2021/day6/input.txt") as f:
        fish = f.read().split(',')
        fish = list(map(int, fish))
    
    for i in range(80): #80 days
        fish = [f-1 for f in fish] #wow so simple!
        new = [8] * fish.count(-1)
        fish = [f if f>=0 else 6 for f in fish] #waaaa!?
        fish.extend(new) #there is no way this works so simple
        #print(i)
    print(len(fish))    

main()