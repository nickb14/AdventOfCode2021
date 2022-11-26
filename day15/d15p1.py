import copy

def main():

    grid = [] #assumed square
    
    with open("day15/input.txt") as f:
        line = f.readline()
        while line:
            grid.append(list(map(int, line.rstrip())))
            line = f.readline()
    
    lenGrid = len(grid) #width and height ehe

    paths = []
    finalSum = float("inf")
    paths.append([0, 0, 0]) #first number is total sum, rest of numbers are positions i, j
    while len(paths) > 0:
        temp = []
        for p in paths:
            sum = p[0]
            i = p[1]
            j = p[2]
            if i+1 != lenGrid:
                temp.append([sum+grid[i+1][j], i+1, j]) #only going down or right
            if j+1 != lenGrid:
                temp.append([sum+grid[i][j+1], i, j+1])
            if i+1 == lenGrid and j+1 == lenGrid:
                finalSum = min(finalSum, sum)
        paths = temp
        paths.sort(key=sortBySums)
        paths = paths[:500000] #cut of number of paths so that it doesn't take forever, 
            #this is the scary (not well thoguht out) part of my logic
            #500,000 gives the correct answer I believe
        print(paths[0][0]) #IT TOOK LIKE 10 MINUTES THEN INDEX ERRORED BUT IT WORKED I kinda feel bad like I cheesed it
    
    print(finalSum)
    
    #diags = []
    #for i in range(len(grid)*2-1):
    #    diags.append([10] * len(grid))
    #for i in range(len(grid)):
    #    for j in range(len(grid)):
    #        diags[i+j][j] = grid[i][j]
    #for d in diags:
    #    print(d)
    #
    #totpos = []
    #for z in range(len(grid)-1):
    #    totpos.append([])
    #    print(z)
    #    for i in range(len(diags)):
    #        least = min(diags[i])
    #        pos = []
    #        if least != 10:
    #            for j in range(len(diags[0])):
    #                if diags[i][j] == least:
    #                    pos.append(j)
    #                    diags[i][j] = 10
    #        totpos[z].append(pos)
    # 
    #for z in range(len(totpos)):
    #    print(z)
    #    for i in range(len(totpos[z])):
    #        print(totpos[z][i])

    #for l in range(10):
    #    n = findPath(0, 0, 0, l, grid)
    #    if n != -1:
    #        break
    #print(n)

def sortBySums(p):
    return p[0]

def findPath(i, j, n, l, grid):
    try:
        ni = grid[i+1][j]
    except:
        ni = 10
    try:
        nj = grid[i][j+1]
    except:
        nj = 10
    
    if i+2 == len(grid) and j+1 == len(grid[0]):
        return n+ni
    elif i+1 == len(grid) and j+2 == len(grid[0]):
        return n+nj
    
    n1, n2 = -1, -1
    if ni <= l:
        n1 = findPath(i+1, j, n+ni, l, grid)
    if nj <= l:
        n2 = findPath(i, j+1, n+nj, l, grid)
    n = min(n1, n2)
    if n1 == -1 and n2 == -1:
        return -1
    elif n1 != -1 and n2 != -1:
        return min(n1, n2)
    else:
        return max(n1, n2)

main()