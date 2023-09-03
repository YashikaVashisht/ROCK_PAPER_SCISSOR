import  random as rd
def start():
    user_choice=input("Enter your choice(ROCK,PAPER or SCISSORS:)")

    options=['ROCK','PAPER','SCISSOR']
    global computer_choice
    computer_choice = rd.choice(options)
    print("computer's choice:",computer_choice)
    check(user_choice)

def check(user_choice):
    if user_choice in ['ROCK','PAPER','SCISSOR','rock','paper','scissor'] :
        condition(user_choice)
    else:
        print("You have enter an invalid options")
        print("PLEASE RETRY IT\n")
        start()
def condition(user_choice):
    if user_choice=='ROCK' or user_choice=='rock':
        rock(computer_choice)
    elif user_choice=='PAPER' or user_choice=='paper':
        paper(computer_choice)
    elif user_choice=='SCISSOR' or user_choice=='scissor':
        scissor(computer_choice)
    else:
        start()
def rock(computer_choice):
    if computer_choice=='ROCK':
        print("TIE\n")
    elif computer_choice=='SCISSOR':
        print("YOU LOST\n")
    else:
        print("YOU WIN!!\n")
    start()
def scissor(computer_choice):
    if computer_choice=='ROCK':
        print("YOU LOST\n")
    elif computer_choice=='SCISSOR':
        print("TIE\n")
    else:
        print("YOU WIN!!\n")
    start()
def paper(computer_choice):
    if computer_choice=='ROCK':
        print("YOU WON\n")
    elif computer_choice=='SCISSOR':
        print("YOU LOST\n")
    else:
        print("TIE\n")
    start()


start()
