def tile_1_1():
#getur farið N.
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        tile_1_2()
    else:
        print("Not a valid direction!")
        tile_1_1()
    
def tile_1_2():
# getur farið S, E, N.
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        tile_1_3()
    elif direction == "e" or direction == "E":
        tile_2_2()
    elif direction == "s" or direction == "S":
        tile_1_1()
    else:
        print("Not a valid direction!")
        tile_1_2()
        
def tile_1_3():
# getur farið S, E.
    print("You can travel: (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "e" or direction == "E":
        tile_2_3()
    elif direction == "s" or direction == "S":
        tile_1_2()
    else:
        print("Not a valid direction!")
        tile_1_3()

def tile_2_1():
# getur farið N.
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        tile_2_2()
    else:
        print("Not a valid direction!")
        tile_2_1()

def tile_2_2():
# getur farið W, S.
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    if direction == "w" or direction == "W":
        tile_1_2()
    elif direction == "s" or direction == "S":
        tile_2_1()
    else:
        print("Not a valid direction!")
        tile_2_2()

def tile_2_3():
# getur farið W, E.
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ")
    if direction == "w" or direction == "W":
        tile_1_3()
    elif direction == "e" or direction == "E":
        tile_3_3()
    else:
        print("Not a valid direction!")
        tile_2_3()

def tile_3_1():
# Victory.
    print("Victory!")

def tile_3_2():
# getur farið S, N.
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        tile_3_3()
    elif direction == "s" or direction == "S":
        tile_3_1()
    else:
        print("Not a valid direction!")
        tile_3_2()

def tile_3_3():
# getur farið W, S.
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    if direction == "w" or direction == "W":
        tile_2_3()
    elif direction == "s" or direction == "S":
        tile_3_2()
    else:
        print("Not a valid direction!")
        tile_3_3()

tile_1_1()

#https://github.com/solons20/TileTraveller.git