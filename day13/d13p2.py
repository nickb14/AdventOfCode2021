#bro don't even it is very messy here

def main():

    data = []
    with open("day13/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line.rstrip())
            line = f.readline()
    
    rows, columns = 0, 0
    gap = data.index("")
    points = []
    for i in range(gap):
        point = tuple(map(int, data[i].split(',')))
        rows = max(point[0], rows)
        columns = max(point[1], columns)
        points.append(point)
    
    rows += 1
    columns += 1
    grid = [[0 for i in range(columns)] for j in range(rows)]
    for point in points:
        grid[point[0]][point[1]] = 1
    
    for i in range(gap+1, len(data)):
        line = data[i]
        fold = int(line[13:]) #don't mind the 13
        if line[11] == 'x': #or the 11
            for r in range(fold+1, len(grid)):
                row = grid[r]
                mirror = grid[2*fold-r]
                for i in range(len(row)):
                    if row[i] == 1:
                        mirror[i] = 1
                grid[2*fold-r] = mirror
            grid = grid[:fold]
        else:
            for r in range(len(grid)):
                row = grid[r]
                for i in range(fold+1, len(row)):
                    point = row[i]
                    mirror = row[2*fold-i]
                    if point == 1:
                        grid[r][2*fold-i] = 1
                grid[r] = grid[r][:fold]
    
    rows = len(grid)
    columns = len(grid[0])
    ughIHaveToFixHowItLooks = [[0 for i in range(rows)] for j in range(columns)]
    for r in range(rows):
        for i in range(columns):
            if grid[r][i] == 0:
                ughIHaveToFixHowItLooks[i][r] = ' '
            else:
                ughIHaveToFixHowItLooks[i][r] = '#'
    for row in ughIHaveToFixHowItLooks:
        print(row)

main()