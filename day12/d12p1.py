def main():

    data = []
    with open("day12/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line.rstrip())
            line = f.readline()
    
    map = {}
    for line in data:
        i = line.index("-")
        s = line[:i] #"start" cave
        f = line[i+1:] #"finish" cave
        addPath(s, f, map)
        addPath(f, s, map)
    
    paths = findPath("start", set(), map)

    print(paths)

def addPath(s, f, map):
    if s in map.keys():
            map[s].append(f)
    else:
        map[s] = [f]

def findPath(s, path, map):
    if s == "end":
        return 1
    if s.islower():
        path = path.copy()
        path.add(s)
    
    paths = 0
    for f in map[s]:
        if f not in path:
            paths += findPath(f, path, map)
    return paths

main()