import random
name=input("ENTER YOUR NAME  ---  ")
print("WELCOME",name,"!")
print("-----------------------")
print("try to give best in your 10 attempts !!")

print("All the best ! 👍🏻👍🏻👍🏻", name,'ji !')
def Hang_man_game():
    list_of_words=['google','hangman','london','india','archana','computer']
    word=random.choice(list_of_words)
    turns=10
    your_guess=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')


    while len(word)>0:
        main_word=""
        missed=0

        for letter in word:
            if letter in your_guess:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print('YOU WON CONGRAGULSTION 🥳🥳🥳🥳🥳🥳!!!!')
            break
        print("guess the word",main_word)
        guess=input()

        if guess in valid_entry:
            your_guess=your_guess+guess
        else:
            print("Enter valid charecter")
            guess=input()
        if guess not in word:
            turns=turns-1
        else:
            turns=turns-1

            if turns==9:
                print("9 turns is left !!!")
                print("-------------------")
                print("          o         ")
            if turns==8:
                print("8 turns is left !!!")
                print("-------------------")
                print("          o           ")
                print("          |           ")
            if turns==7:
                print("7 turns is left !!!")
                print("---------------------")
                print("           o          ")
                print("           |          ")
                print("          /           ")
            if turns==6:
                print("6 tirns is left !!!")
                print("--------------------")
                print("           o         ")
                print("           |         ")
                print("          / \        ")
            if turns==5:
                print("5 turns is left !!!")
                print("-------------------")
                print("           \o          ")
                print("            |          ")
                print("           / \         ")
            if turns==4:
                print("4 turns is left !!!")
                print("--------------------")
                print("           \o/          ")
                print("            |          ")
                print("           / \         ")
            if turns==3:
                print("3 turns is left !!!")
                print("---------------------")
                print("           \o/  |          ")
                print("            |          ")
                print("           / \          ")
            if turns==2:
                print("2 turns is left !!!")
                print("--------------------")
                print("           \o/__|        ")
                print("            |          ")
                print("           / \         ")
            if turns==1:
                print("only 1 turns is left !!!")
                print("--------------------")
                print("      __       ")
                print("                |      ")
                print("                |      ")
                print("           \o/__|      ")
                print("            |          ")
                print("           / \         ")
            if turns==1:
                print(" you loose the game  !!!")
                print(" now your good man is die 😔😔😔😔")
                print("--------------------")
                print("   Hanged😔__       ")
                print("               |      ")
                print("               |      ")
                print("            o__|      ")
                print("           /|\          ")
                print("           / \         ")
                break
Hang_man_game()