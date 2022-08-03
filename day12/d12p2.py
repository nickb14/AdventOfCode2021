def main():

    data = []
    with open("day12/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line.rstrip())
            line = f.readline()
    
    map = {}
    smalls = set()
    for line in data:
        i = line.index("-")
        s = line[:i] #"start" cave
        f = line[i+1:] #"finish" cave
        addPath(s, f, map, smalls)
        addPath(f, s, map, smalls)
    
    smalls.remove("start")
    smalls = list(smalls)
    paths = findPath("start", smalls, "start", map)
    
    for small in smalls:
        smalls.append(small)
        paths += findPath("start", smalls, small, map)
        smalls.pop(-1)

    print(paths)

def addPath(s, f, map, smalls):
    if s in map.keys():
            map[s].append(f)
    else:
        map[s] = [f]
    if s.islower():
            smalls.add(s)

def findPath(s, smalls, double, map):
    if s == "end" and double not in smalls:
        return 1
    if s in smalls:
        smalls = smalls.copy()
        smalls.remove(s)

    paths = 0
    for f in map[s]:
        if f.isupper() or f in smalls:
            paths += findPath(f, smalls, double, map)
    return paths

main()