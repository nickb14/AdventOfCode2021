import copy

def main():

    grid = [] #assumed square
    
    with open("day15/input.txt") as f:
        line = f.readline()
        while line:
            grid.append(list(map(int, line.rstrip())))
            line = f.readline()
    
    grids = []
    grids.append(grid)
    for i in range(8): #8 more plus1's to get to bottom corner of 5x5
        grids.append(plus1(grids[i]))
    
    lenGrid = len(grid) #width and height ehe

    grid = [] #reset
    for z in range(5): #5x5
        for i in range(lenGrid):
            newRow = grids[z][i] + grids[z+1][i] + grids[z+2][i] + grids[z+3][i] + grids[z+4][i]
            grid.append(newRow)
 
    lenGrid = len(grid) #bigger grid

    paths = [[] for _ in range(lenGrid*2-1)] #number of moves to get to bottom corner, only moving down or right
    paths[0].append([0, 0, 0]) #first number is total sum, rest of numbers are positions i, j

    z = 1
    while z < lenGrid*2-1: #doesn't start at zero because that path was appended above
        panic = 0
        for p in paths[z-1]:
            sum = p[0]
            i = p[1]
            j = p[2]
            if i+1 != lenGrid:
                paths[z].append([sum+grid[i+1][j], i+1, j]) #only going down or right
            if j+1 != lenGrid:
                paths[z].append([sum+grid[i][j+1], i, j+1])
            if i != 0:
                new = sum + grid[i-1][j] #aaaand it seems going backwards has to be an option
                index = findIndex(i-1, j, paths[z-2])
                if new < paths[z-2][index][0]:
                    paths[z-2][index] = [new, i-1, j]
                    panic = 2
            if j != 0:
                new = sum + grid[i][j-1]
                index = findIndex(i, j-1, paths[z-2])
                if new < paths[z-2][index][0]:
                    paths[z-2][index] = [new, i, j-1]
                    panic = 2
        paths[z].sort(key=sortBySums)

        duplicates = [] #how (stupid) of me to not consider duplicates such as these aiya
        for x in range(len(paths[z])): #more loops but a much better approach to shortening the number of paths, praise
            for y in range(x+1, len(paths[z])):
                if paths[z][x][1] == paths[z][y][1] and paths[z][x][2] == paths[z][y][2]:
                    duplicates.append(y)
        duplicates = list(set(duplicates)) #removing duplicates in "duplictaes" lol
        duplicates.sort(reverse=True)
        for d in duplicates:
            paths[z].pop(d)
        
        #print(paths[z][0][0])
        z += 1 - panic
    
    print(paths[-1][0][0]) #it took like 15 minutes but I don't care anymore it worked
    
def sortBySums(p):
    return p[0]

def plus1(grid):
    temp = copy.deepcopy(grid)
    lenGrid = len(grid)
    for i in range(lenGrid):
        for j in range(lenGrid):
            temp[i][j] += 1
            if temp[i][j] == 10:
                temp[i][j] = 1
    return temp

def findIndex(i, j, paths):
    for index in range(len(paths)):
        if paths[index][1] == i and paths[index][2] == j:
            return index

main()