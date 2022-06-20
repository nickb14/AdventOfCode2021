def main():

    heightmap = []
    b = 9 #border of 9s
    
    with open("day09/input.txt") as f:
        line = f.readline()
        while line:
            heightmap.append([b] + list(map(int, line.rstrip())) + [b])
            line = f.readline()
    
    width = len(heightmap[0])
    heightmap.insert(0, [b] * width)
    heightmap.append([b] * width)
    length = len(heightmap)

    basins = []
    for i in range(1, length-1):
        for j in range(1, width-1):
            basins.append(check(i, j, heightmap))
    
    basins.sort()
    print(basins[-1] * basins[-2] * basins[-3])
    
#recursive, check 4 adjecent points, stop if 9, set point to 9 after
def check(i, j, heightmap): #not sure if copy of list "heightmap" is being made or not hopefully not?
    if heightmap[i][j] != 9:
        heightmap[i][j] = 9

        tot = 0
        tot += check(i-1, j, heightmap)
        tot += check(i+1, j, heightmap)
        tot += check(i, j-1, heightmap)
        tot += check(i, j+1, heightmap)
        return tot + 1
    else:
        return 0

main()