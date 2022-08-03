#I forgot how to do this brah

def main():

    grid = []
    steps = 100
    
    with open("day11/input.txt") as f:
        line = f.readline()
        while line:
            grid.append(list(map(int, line.rstrip())))
            line = f.readline()

    tot = 0
    
    for r in range(steps):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += 1
                if grid[i][j] == 10:
                    tot += flash(i, j, grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] >= 10):
                    grid[i][j] = 0
        #print("step " + str(r+1))
        #for row in grid:
        #    print(row)
    
    print(tot)

def flash(i, j, grid):
    num = 1
    for x in range(i-1, i+2):
        if x < 0:
            continue
        for y in range(j-1, j+2):
            if y < 0:
                continue
            try:
                grid[x][y] += 1
                if grid[x][y] == 10:
                    num += flash(x, y, grid)
            except:
                pass
    return num



main()