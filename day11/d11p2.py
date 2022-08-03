def main():

    grid = []
    steps = 500
    
    with open("day11/input.txt") as f:
        line = f.readline()
        while line:
            grid.append(list(map(int, line.rstrip())))
            line = f.readline()
    
    allFlash = False
    for r in range(steps):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += 1
                if grid[i][j] == 10:
                    flash(i, j, grid)
        allFlash = True
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] >= 10):
                    grid[i][j] = 0
                else:
                    allFlash = False
        if allFlash:
            print(r+1)
            break

def flash(i, j, grid):
    for x in range(i-1, i+2):
        if x < 0:
            continue
        for y in range(j-1, j+2):
            if y < 0:
                continue
            try:
                grid[x][y] += 1
                if grid[x][y] == 10:
                    flash(x, y, grid)
            except:
                pass



main()