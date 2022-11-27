def main():

    with open("day16/input.txt") as f:
        hexi = f.read()
    
    bina = bin(int(hexi, 16))[2:].zfill(len(hexi)*4) #binary string, chop off 0b at front and add back zeros at front
    
    sum = 0

    i = 0
    while i <= bina.rfind('1'):
        version = int(bina[i:i+3], 2)
        sum += version #just some addition, seems like the only important thing for part 1...
        type = int(bina[i+3:i+6], 2)
        i += 6
        if type == 4:
            while int(bina[i]) == 1:
                #the literal value doesn't matter for now
                i += 5
            i += 5 #then big loop starts over
        else:
            if int(bina[i]) == 0:
                #I don't know if this length of subpackets matters...
                i += 16
            else:
                #I am also not certain this number of subpackets matters...
                i += 12
    
    print(sum)

main()