import collections

def main():

    data = []
    steps = 10

    with open("day14/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line.rstrip())
            line = f.readline()
    
    poly = data[0]

    insertions = {}
    for i in range(2, len(data)):
        line = data[i]
        insertions[line[0:2]] = line[6]
    
    for s in range(steps):
        inserts = ""
        for i in range(len(poly)-1):
            inserts += insertions[poly[i:i+2]]
        for i in range(len(inserts)):
            pos = i*2 + 1
            poly = poly[:pos] + inserts[i] + poly[pos:]
    
    counts = collections.defaultdict(int)
    for p in poly:
        counts[p] += 1

    sortedElements = sorted(counts, key=counts.get) #keys of dict, sorted by their values ?
    print(counts[sortedElements[-1]] - counts[sortedElements[0]])

main()