from User import User
from SkyKingdom import SkyKingdom
from FinalBoss import FinalBoss
from termcolor import *
import time


# general task functions + non sequential functions
def colorize(text, user_class):
    text = colored(text, user_class.returnColor(), attrs=['bold'])
    return text

def typeWriter(text, user = None, lag = 0.02):
    text = list(str(text))
    if user == None:
        for letter in text:
            time.sleep(lag)
            print(letter,end='',flush=True)
    else:
        for letter in text:
            time.sleep(lag)
            print(colorize(letter, user),end='',flush=True)

# game logic functions (in order)
def startofgame_greetings():
    greeting = 'Welcome to the virtual world.'
    typeWriter(greeting)
    print('\n')


def get_user_name():
    typeWriter('What is your name? ')
    user_name = input()
    return str(user_name)


def get_user_class_choice():
    user_choice = ''
    print('\n')
    typeWriter('Choose your class (Type \'A\', \'B\', or \'C\')')
    print('\n')
    while user_choice != 'A' and user_choice != 'B' and user_choice != 'C':
        typeWriter('A: Archer\nB: Sorcerer\nC: Assassin\n\n')
        user_choice = input()
    return user_choice


def initiation(user_name, user):
    typeWriter(user_name + ', your goal is to make it out of this world alive.\n')
    typeWriter('You have chosen ')
    typeWriter(user.returnType(), user)

    typeWriter('\nYour weapon of choice is ')
    typeWriter(user.returnWeapon(), user)

    typeWriter('\nNumber of Lives: ')
    typeWriter(user.returnLives(), user)


def show_additional_stats(user):
    typeWriter('\nName: ')
    typeWriter(user.returnName(),user)

    typeWriter('\nType: ')
    typeWriter(user.returnType(), user)

    typeWriter('\nWeapon: ')
    typeWriter(user.returnWeapon(), user)

    typeWriter('\nDamage: ')
    typeWriter(user.returnDamage(), user)

    typeWriter('\nRange: ')
    typeWriter(user.returnRange(), user)

    typeWriter('\nStealth: ')
    typeWriter(user.returnStealth(), user)

def choosePath(user_class):
    typeWriter('\n\nStory here.......')
    chosen_path = ''
    while chosen_path != 'A' and chosen_path != 'B' and chosen_path != 'C':
        typeWriter('Which realm would you like to enter?'
                            '\n A) Sky Kingdom \n B) The Underworld \n C) The Jungle\n\n')
        chosen_path = input()
    return chosen_path

def main():

    startofgame_greetings() # greet the user

    user_name = get_user_name() # get the user's name
    user_class_choice = get_user_class_choice() # get the user's class choice (A, B, C)
    user = User(user_name, user_class_choice) # create the User class

    initiation(user_name, user) # initiate the user based on class attributes and user name and start game

    see_additional_stats = ''
    while see_additional_stats != 'Y' and see_additional_stats != 'N':
        typeWriter('\nWould you like to see your additional stats? (Y or N)\n')
        see_additional_stats = input()
    if see_additional_stats == 'Y':
        show_additional_stats(user)

    typeWriter('\n\nYou activate the gem to return home')
    typeWriter('...\n\n', lag=1)
    typeWriter('What??? \nInstead of returning home, you are teleported to a strange'
                   ' arena. \nLights flash on and you are ushered into the middle.'
                   '\n\n"The next challenger is ')
    typeWriter(user.returnName(), user=user)
    typeWriter('! Let\'s see if he has what it takes to defeat the Grandmaster!"\n\n')
    world = FinalBoss(user)
    world.run()
    typeWriter('\n\nThanks for playing!')
    typeWriter('\n\nPlay again? (Y or N)\n')
    playagain = input()
    if playagain:
        main()


main()

def main2():
    user=User("B", "B")
    world = FinalBoss(user)
    user_result = world.run()

#main2()
