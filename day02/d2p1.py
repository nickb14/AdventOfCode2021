def main():
    dirs = []
    with open("day02/input.txt") as f:
        line = f.readline()
        while line:
            dirs.append(lineToDir(line))
            line = f.readline()
    
    hori = 0
    depth = 0
    for dir in dirs:
        if dir[0] == 0:
            hori += dir[1]
        else:
            depth += dir[1]
    
    product = hori * depth
    print(product)

#returns tuple, first value 0 for forward, 1 for up/down; second value for amount (signed +/-)
def lineToDir(line):
    i = line.index(' ')
    x = int(line[i+1:i+2]) #newlines at end of lines annoying
    dir = line[:i]
    if dir == "forward":
        return (0, x)
    else:
        if dir == "up":
            x *= -1
        return (1, x)

main()