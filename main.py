import random

def rps_input(rps_list):
    c1 = input("Rock,Paper,Scissors :").capitalize()
    c2 = random.choice(rps_list)
    return c1,c2

def rps(p1, p2):
    if p1==p2:
        return "Draw!"
    elif p1=="Rock":
        if p2=="Scissors":
            return "You Won!"
        elif p2=="Paper":
            return "You Lost!"
    elif p1=="Scissors":
        if p2=="Rock":
            return "You Lost!"
        elif p2=="Paper":
            return "You Won!"
    elif p1=="Paper":
        if p2=="Rock":
            return "You Won!"
        elif p2=="Scissors":
            return "You Lost!"