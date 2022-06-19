#I forgot how to do this brah

def main():

    heightmap = []
    
    with open("day09/input.txt") as f:
        line = f.readline()
        while line:
            heightmap.append([10] + list(map(int, line.rstrip())) + [10])
            line = f.readline()
    
    width = len(heightmap[0])
    heightmap.insert(0, [10] * width) #bordered by 10s because I want to
    heightmap.append([10] * width)
    length = len(heightmap)

    total = 0
    for i in range(1, length-1):
        for j in range(1, width-1):
            h = heightmap[i][j]
            #the absolute laziest solution, so any unecessary checks for less than...?
            if h < heightmap[i-1][j] and h < heightmap[i+1][j] and h < heightmap[i][j-1] and h < heightmap[i][j+1]:
                total += h + 1
    
    print(total)

main()