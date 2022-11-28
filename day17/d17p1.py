def main():

    with open("day17/input.txt") as f:
        line = f.read()
    
    yequals = line.rfind("y=")
    ydotdot = line.rfind("..")
    ymin = int(line[yequals+2:ydotdot])
    #ymax = int(line[ydotdot+2:])
    
    #pretty sure this works as long as ymin is nagative:
    vymax = ymin*-1-1

    #and then it's just the triangle number
    yahboi = 0
    for i in range(vymax+1):
        yahboi += i
    
    print(yahboi)

main()