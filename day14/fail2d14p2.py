import collections

def main():

    for steps in range(1, 25):

        data = []

        with open("day14/input.txt") as f:
            line = f.readline()
            while line:
                data.append(line.rstrip())
                line = f.readline()
        
        poly = data[0]

        insertions1 = {}
        for i in range(2, len(data)):
            line = data[i]
            insertions1[line[0:2]] = line[6]
        
        insertions = insertions1
        #for k in insertions1.keys():
        #    a = k[0]
        #    b = insertions1[k]
        #    c = k[1]
        #    insertions[k] = a + insertions1[a+b] + b + insertions1[b+c] + c
            
        counts = collections.defaultdict(int)
        for p in poly:
            counts[p] += 1
        
        for i in range(len(poly)-1):
            insert(poly[i], poly[i+1], 0, insertions, counts, steps)

        sortedElements = sorted(counts, key=counts.get) #keys of dict, sorted by their values ?
        print(steps)
        print("    " + sortedElements[-1] + " = " + str(counts[sortedElements[-1]]))
        print("    " + sortedElements[0] + " = " + str(counts[sortedElements[0]]))
        print("    " + str(counts[sortedElements[-1]] - counts[sortedElements[0]]))

def insert(a, c, s, insertions, counts, steps):
    b = insertions[a+c]
    count(b, counts)
    s += 1
    if s == steps:
        return
    insert(a, b, s, insertions, counts, steps)
    insert(b, c, s, insertions, counts, steps)

def count(b, counts):
    for p in b:
        counts[p] += 1

main()