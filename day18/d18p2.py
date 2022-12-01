import copy

def main():

    snailnums = []

    with open("day18/input.txt") as f:
        line = f.readline()
        while line:
            snailnums.append(eval(line))
            line = f.readline()
    
    greatest = 0
    for s0 in snailnums:
        for s1 in snailnums:
            if s0 != s1:
                #I'll say it again, I hate it here, all I needed to do was add copy but that took like 30 minutes to figure out
                dictnum = reduce(listToDict(copy.deepcopy([s0, s1])))
                greatest = max(greatest, magnitudeDict(dictnum, 9))
    
    print(greatest)


def reduce(dictnum):
    i = 0
    for strnum, num in dictnum.items(): #explode!
        if isinstance(num, list):
            keys = list(dictnum)
            if i != 0:
                key = keys[i-1]
                if isinstance(dictnum[key], list): #if there are 2 explodes next to each other...!
                    dictnum[key][1] += num[0]
                else:
                    dictnum[key] += num[0]
            if i+1 != len(keys):
                key = keys[i+1]
                if isinstance(dictnum[key], list): #same, 2 explodes...!
                    dictnum[key][0] += num[1]
                else:
                    dictnum[key] += num[1]
            dictnum[strnum] = 0
            return reduce(dictnum)
        i += 1
    for strnum, num in dictnum.items(): #split!
        if num >= 10:
            r1 = num//2
            if r1 == num/2:
                r2 = r1
            else:
                r2 = r1 + 1
            if len(strnum) == 20: #snailnum (len of 8) better stay as the variable name then...
                dictnum[strnum] = [r1, r2]
            else:
                temp = {}
                for newstrnum, newnum in dictnum.items():
                    if newstrnum == strnum:
                        temp[strnum + "[0]"] = r1
                        temp[strnum + "[1]"] = r2
                    else:
                        temp[newstrnum] = newnum
                dictnum = temp
            return reduce(dictnum)
    return dictnum

def listToDict(snailnum): #basically a complicated flattening of the list
    dictnum = {}
    for i in range(16): #it will only ever be 4 lists within lists?
        x = bin(i)[2:].zfill(4)
        strnum = "snailnum"
        for depth in range(4):
            strnum += "[" + x[depth] + "]"
            num = eval(strnum)
            if isinstance(num, int) or depth == 3:
                dictnum[strnum] = num
                break
    return dictnum

def dictToList(dictnum, i):
    if len(dictnum) == 1:
        return list(dictnum.values())[0] #idk
    dictnum0, dictnum1 = {}, {} #recursive in half type stuff
    for strnum, num in dictnum.items():
        if strnum[i] == '0':
            dictnum0[strnum] = num
        else:
            dictnum1[strnum] = num
    l = dictToList(dictnum0, i+3)
    r = dictToList(dictnum1, i+3)
    return [l, r]

def magnitudeDict(dictnum, i): #I was too lazy to make a magnitudeList don't @ me
    if len(dictnum) == 1:
        return list(dictnum.values())[0] #idk
    dictnum0, dictnum1 = {}, {} #recursive in half type stuff
    for strnum, num in dictnum.items():
        if strnum[i] == '0':
            dictnum0[strnum] = num
        else:
            dictnum1[strnum] = num
    l = magnitudeDict(dictnum0, i+3)
    r = magnitudeDict(dictnum1, i+3)
    return 3*l + 2*r

main()