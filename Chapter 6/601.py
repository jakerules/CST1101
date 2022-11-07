dir = "E"
def turn_clockwise(dir):
    if dir == "N":
        return "E"
    elif dir == "E":
        return "S"
    elif dir == "S":
        return "W"
    elif dir == "W":
        return "N"
    else:
        print("Invalid")
        
print(turn_clockwise(dir))