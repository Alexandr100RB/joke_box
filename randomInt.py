import random


# пока это всё не работает
def guessInt():
    numberToGuess=random.randint(1,10)
    userGuess=-1

    print("Угадай число от 1 до 10")
    while userGuess!=numberToGuess:
        userGuess=int(input(""))
        if userGuess > numberToGuess:
            print("Число должно быть меньше!")
        elif userGuess < numberToGuess:
            print("Число должно быть больше!")
        else:
            print("Вы угадали, это число " + str(numberToGuess))
            #Конец игры - выйти из цикла while
            break

