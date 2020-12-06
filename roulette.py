from random import randrange
from math import ceil

money = 1000
continue_play = True
name = -1 

while name == -1:
    name = input("What's your name ?")
    try :
        name = str(name)
    except TypeError :
        print("Sorry but this name isn't acceptable, try with a another name :")
        name = -1
        continue
    
print(f"Hello and welcome {name}, you have {money}$. Let's start !")
#Here did a small modif, used f method    
while continue_play :
    # Choosing the number you want to bet on 
    bet_choice = -1
    while bet_choice < 0 or bet_choice > 49 :
        bet_choice = input("Choose a number to bet on, between 0 to 49 :")
        try : 
            bet_choice = int(bet_choice)
        except ValueError :
            print("Sorry but your choice isn't a number, try with another value please :")
            bet_choice = -1
            continue
        if bet_choice < 0 :
            print("Sorry we don't accept numbers inferior to 0, try again ")
        if bet_choice > 49 :
            print("Sorry we don't accept numbers superior to 49, try again ")
    
    # Choosing how much you want to bet 
    bet_money = 0
    while bet_money <= 0 or bet_money > money :
        bet_money = input("Choose how much you want to bet please :")
        try :
            bet_money = int(bet_money)
        except ValueError :
            print("Sorry but your choice isn't a number, try with another value please :")
            bet_money = -1
            continue
        if bet_money < 0 :
            print("Sorry but you can't bet less than 1$, try again :")
        if bet_money > money :
            print(f"Sorry but you don't have enough money to place a bet this high, you only have {money}$")
    
    # Sorting winning number         
    winning_number = randrange(50)        
    print("The roulette is spinning and the lucky number is...", winning_number)
    
    # Gains or Loses
    if bet_choice == winning_number :
        print("You're in luck today you just won", bet_money * 3,"$")
        money += bet_money * 3
    elif (bet_choice % 2) == (winning_number % 2) :
        bet_money = ceil(bet_money * 0.5)
        print ("Congrats !!! you won", bet_money,"$")
        money += bet_money
    else :
        print("Sorry, you'll maybe have more luck next time !")
        money -= bet_money
    
    #continue playing or not 
    if money <= 0 :
        print("Sorry you don't have any money, see you next time")
        continue_play = False   
    else :
        question = True
        while question :
            print("You have ", money,"$")
            quit = input(f"{name}, do you want to exist the casino (y/n) ?")
            if quit.lower() == "y" :
                print("Ok not problem, see you next time")
                continue_play = False
                question = False
            elif quit.lower() == "n" :
                print("That's what we want to hear, Let's go again !!!")
                question = False
            else :
                print("Sorry we didn't get that, come again ")
                question = True
                