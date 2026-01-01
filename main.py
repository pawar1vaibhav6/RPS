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
        
def main():
    sys_score = 0
    y_score = 0
    rps_list = ["Rock", "Paper", "Scissors"]
    while True:
        a1, a2 = rps_input(rps_list)
        if a1 in rps_list:
            result = rps(a1, a2)
            print(a2)
            print(result)
        else:
            print("Invalid Input")
            continue
        if result == 'You Won!':
            y_score += 1
        elif result == 'You Lost!':
            sys_score += 1
        print("Your Score:{}".format(y_score))
        print("Opponent Score:{}".format(sys_score))
        while True:
            again = input("Play again (y/n): ").lower()
            if again in ("y", "n"):
                break
            print("Please enter y or n")

        if again == "n":
            print("Thanks for Playing 😊")
            break


if __name__=='__main__':
    main()