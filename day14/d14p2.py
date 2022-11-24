import collections

def main():

    data = []
    steps = 40

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
    
    counts = collections.defaultdict(int)
    for p in poly:
        counts[p] += 1
    
    pairs = collections.defaultdict(int)
    for i in range(len(poly)-1):
        pairs[poly[i:i+2]] += 1
    
    for s in range(steps):
        newPairs = collections.defaultdict(int)
        for pair in pairs:
            insert = insertions[pair]
            num = pairs[pair]
            counts[insert] += num
            newPairs[pair[0] + insert] += num
            newPairs[insert + pair[1]] += num
        pairs = newPairs

    sortedElements = sorted(counts, key=counts.get) #keys of dict, sorted by their values ?
    print(counts[sortedElements[-1]] - counts[sortedElements[0]])

main()