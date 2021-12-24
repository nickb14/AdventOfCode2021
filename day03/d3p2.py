def main():
    lines = []
    with open("/workspace/AdventOfCode2021/day03/input.txt") as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    
    bits = range(len(lines[-1])) #range of number of bits
    
    oxyList = lines.copy() #everything happens twice kinda lol, messy?
    co2List = lines.copy() #could make some functions but too lazy

    for i in bits:
        commonOxy = 0
        commonCo2 = 0

        for line in oxyList:
            if line[i] == '0':
                commonOxy -= 1
            else:
                commonOxy += 1
        for line in co2List:
            if line[i] == '0':
                commonCo2 -= 1
            else:
                commonCo2 += 1
        
        if commonOxy < 0:
            commonOxy = 0
        else:
            commonOxy = 1
        if commonCo2 < 0:
            commonCo2 = 0
        else:
            commonCo2 = 1
        
        temp = oxyList.copy()
        for line in oxyList:
            if line[i] != str(commonOxy): #remove if NOT the common
                temp.remove(line)
        oxyList = temp.copy()
        if len(co2List) > 1: #extra check needed to not remove the last number from co2List
            temp = co2List.copy()
            for line in co2List:
                if line[i] == str(commonCo2): #remove if IS the common
                    temp.remove(line)
            co2List = temp.copy()
    
    oxy = int(oxyList[0], 2) #should be only one number left in the list
    co2 = int(co2List[0], 2)
    product = oxy * co2
    print(product)

main()