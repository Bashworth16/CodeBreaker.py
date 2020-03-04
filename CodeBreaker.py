import string
import random


def get_name():
    name = input("Hello, User! What is your name?!: ")
    return name

def robo_name():
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    vowels = ["A", "E", "I", "O", "U", "Y"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(numbers)

def formal_greeting(n, rn):
    print("Nice to meet you, " + n + ". My name is " + rn + ".")


def want_to_play():
    play = True
    while play:
        to_play = input(user_name + ", We need your help. We are trying to crack a series of 5 digit codes made up of numbers between 1 and 10.\n Every ten codes solved you will graduate to help the next bot. Will you help us?! [Y/N]: ")
        if to_play == "Y":
            print("Great! Lets get to work!")
            play = False
        if to_play == "N":
            exit()
        if to_play != "Y":
            print("Invalid Entry. Please Try Again!")

def get_code():
    code = random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)
    return code

def compare_guesses():
    guess_one = input("First Number?: ")

    guess_two = input("Second Number?: ")
    guess_three = input("Third Number?: ")
    guess_four = input("Fourth Number?: ")
    guess_five = input("Fifth Number?: ")
    g = int(guess_one), int(guess_two), int(guess_three), int(guess_four), int(guess_five)
    print(g)

    if g[0] == code[0]:
        print("OK!")
    if g[0] > code[0]:
        print(str(g[0]) + " Lower. ")
    if g[0] < code[0]:
        print(str(g[0]) + " Higher. ")
    if g[1] == code[1]:
        print("OK!")
    if g[1] > code[1]:
        print(str(g[1]) + " Lower. ")
    if g[1] < code[1]:
        print(str(g[1]) + " Higher ")
    if g[2] == code[2]:
        print("OK!")
    if g[2] > code[2]:
        print(str(g[2]) + " Lower. ")
    if g[2] < code[2]:
        print(str(g[2]) + " Higher. ")
    if g[3] == code[3]:
        print("OK!")
    if g[3] > code[3]:
        print(str(g[3]) + " Lower. ")
    if g[3] < code[3]:
        print(str(g[3]) + " Higher. ")
    if g[4] == code[4]:
        print("OK!")
    if g[4] > code[4]:
        print(str(g[4]) + " Lower. ")
    if g[4] < code[4]:
        print(str(g[4]) + " Higher. ")
    if g[0:4] == code[0:4]:
        print("Great! We Did It!")
        return get_code()
    else:
        return compare_guesses()


user_name = get_name()
robo = robo_name()
formal_greeting(user_name, robo)
play = want_to_play()
code = get_code()
compare = compare_guesses()