import random


def guessInt():
    NumberToGuess=random.randint(1,10)
    userGuess=-1

    while userGuess!=NumberToGuess:
        userGuess=int(input("Угадай число от 1 до 10\n"))
        if userGuess > NumberToGuess:
            print("Число должно быть меньше!")
        elif userGuess < NumberToGuess:
            print("Число должно быть больше!")
        else:
            print("Вы угадали, это число = " + str(NumberToGuess))
            #Конец игры - выйти из цикла while
            break

