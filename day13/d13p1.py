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
    
    #just the first instruction idc
    for r in range(655+1, rows):
        row = grid[r]
        mirror = grid[2*655-r]
        for i in range(len(row)):
            if row[i] == 1:
                mirror[i] = 1
        grid[2*655-r] = mirror
    
    grid = grid[:655]
    tot = 0
    for row in grid:
        for point in row:
            if point == 1:
                tot += 1
    
    print(tot)
    #that is terrible code and I am not sorry :)

main()