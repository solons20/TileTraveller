posstartx = 1
posstarty = 1
up = 1
right = 1
down = -1
left = -1

def moveallowed(x, y):
    if ((x == 1) and (y == 1)):
        print("N)orth.")
    elif ((x == 1) and (y == 2)):
        print("(N)orth or (E)ast or (S)outh.")
    elif ((x == 1) and (y == 3)):
        print("(E)ast or (S)outh.")
    elif ((x == 2) and (y == 3)):
        print("(E)ast or (W)est.")
    elif ((x == 2) and (y == 2)):
        print("(S)outh or (W)est.")
    elif ((x == 2) and (y == 1)):
        print("(N)orth.")
    elif ((x == 3) and (y == 3)):
        print("(S)outh or (W)est.")
    elif ((x == 3) and (y == 2)):
        print("(N)orth or (S)outh.")
    elif ((x == 3) and (y == 1)):
        print("Victory!")
    
    

def movemade(str):
    if (str == "n" or str == "N"):
        up += 1
    elif (str == "e" or str == "E"):
        right += 1
    elif (str == "s" or str == "S"):
        down -= 1
    elif (str == "w" or str == "W"):
        left -= 1
        
def wrongmove(str):
    if((direct != "n") and (direct != "N") and (direct != "s") and (direct != "S") and (direct != "w") and (direct != "W") and (direct != "e") and (direct != "E"))
        

print("You can travel:", moveallowed(posstartx, posstarty))
direct = input("Direction: prufa ")


