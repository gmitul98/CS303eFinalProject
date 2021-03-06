#Importing other python files
"""
This part of the file imports all of the other files that we shall be using, each part referring to a different section of the game
"""
from User import User
from SkyKingdom import SkyKingdom
from Underworld import Underworld
from getaway import getaway
from FinalBoss import FinalBoss
from termcolor import *
import time
import config


# general task functions + non sequential functions
#function definition
def colorize(text, user_class):
    #assignment statement
    text = colored(text, user_class.returnColor(), attrs=['bold'])
    return text

#function defintion with parameters
def boldIt(text):
    text = colored(text,attrs=['bold'])
    return text

#function definition with default parameters
def typeWriter(text, user = None, lag = config.lag, bold = False):
    text = list(str(text))
#if statement
    if user == None:
        #for loop
        for letter in text:
            time.sleep(lag)
            #nested if statement
            if bold:
                #function that calls another function
                print((boldIt(letter)), end='', flush=True)
            else:
                #print statement
                print(letter,end='',flush=True)
    else:
        for letter in text:
            time.sleep(lag)
            print(colorize(letter, user),end='',flush=True)

# game logic functions (in order)
def startofgame_greetings():
    typeWriter('Ahh. The smell of coffee is always the best. \nIt\'s 7am and you\'ve just walked into your local Starbucks.' 
               '\nTo get through your Monday morning, you have to start it off strong.' 
               '\n\nYour\'re up to order: ')
    typeWriter('\n\n"A White Chocolate Mocha please."', bold=True)
    typeWriter('\n\n"Could I get a name for that order?" ', bold=True)

def get_user_name():
    user_name = input()
    return str(user_name)

def inciting_incident(username):
    typeWriter('\n"Okay, ' + username + '. One White Mocha coming right up"\n', bold=True)
    typeWriter('\nYou grab your coffee and go. '
               '\nOn your way out, you see a Nintendo device sprawled on the ground.'
               '\nHmm. Could some kid have left it here?'
               '\nYou should probably give it to the Starbucks employees to handle the situation.'
               '\nWhat do you do? ')
    whatever = input()
    typeWriter('\nYou think about what would happen if you ' + str(whatever.lower()))
    typeWriter('\nYou decide to pick up the Nintendo.'
               '\nAs soon as you touch it, you feel an overwhelming G-Force and you see nothing but white light')
    typeWriter('\n.\n.\n.', lag=0.5)
    typeWriter('\n\nYou finally open your eyes and you are in the middle of a forest.'
               '\nSuddenly a cloaked man with a knife approaches you. He is 20 feet away.'
               '\nYou look down and you see three items. Which one do you pick?\n\n')

def get_user_class_choice():
    user_choice = ''
    while user_choice != 'A' and user_choice != 'B' and user_choice != 'C':
        typeWriter('A: Bow and Arrow\nB: Magic Staff\nC: Poisoned Dagger\n\n')
        user_choice = input().upper()
    return user_choice


def initiation(user_name, user):
    typeWriter(user_name + ', great choice.\n')
    typeWriter('\nYou attack the man with the ' + user.returnWeapon() + ' and defeat him.')
    typeWriter('\nSuddenly, another white light flashes and you seem to have been given'
               ' some mysterious clothes. \nYou feel the power of the ')
    typeWriter(user.returnType(), user)

    typeWriter(' coursing through you and your weapon of choice is ')
    typeWriter(user.returnWeapon(), user)


def show_additional_stats(user):
    typeWriter('\nName: ')
    typeWriter(user.returnName(),user)

    typeWriter('\nLives: ')
    typeWriter(user.returnLives(), user)

    typeWriter('\nType: ')
    typeWriter(user.returnType(), user)

    typeWriter('\nWeapon: ')
    typeWriter(user.returnWeapon(), user)

    typeWriter('\nHealth: ')
    typeWriter(user.returnHealth(), user)

    typeWriter('\nDamage: ')
    typeWriter(user.returnDamage(), user)

    typeWriter('\nRange: ')
    typeWriter(user.returnRange(), user)

    typeWriter('\nStealth: ')
    typeWriter(user.returnStealth(), user)

def choosePath(user_class):
    typeWriter('\n\nYou finally emerge on land and you begin exploring.\nYou eventually come across an ancient text. '
               'It reads:\n -- Scattered around this world are three heavenly gems.'
               ' They are said to allow people to transcend this world. There'
               ' is one in each realm: \nSky Kingdom\nThe Underworld\n'
               'You know this is your one chance to return to reality.\n\n')
    chosen_path = ''
    #While loop
    while chosen_path != 'A' and chosen_path != 'B':
        typeWriter('Which realm would you like to enter?'
                            '\n A) Sky Kingdom \n B) The Underworld\n\n')
        chosen_path = input().upper()
    return chosen_path

def win():
    typeWriter('\n\nThe world around you fades to black and then zones back to reality'
                        '. It is done. The game is won.\n')
def death():
    typeWriter('\n\nYou\'ll never make it back to reality.'
                    'You stumble around as the world starts to fade to black...')

def main():

    startofgame_greetings() # greet the user
    user_name = get_user_name() # get the user's name
    inciting_incident(user_name) #inciting incident
    user_class_choice = get_user_class_choice() # get the user's class choice (A, B, C)
    user = User(user_name, user_class_choice) # create the User class
    initiation(user_name, user) # initiate the user based on class attributes and user name and start game

    see_additional_stats = ''
    while see_additional_stats != 'Y' and see_additional_stats != 'N':
        typeWriter('\nWould you like to see your additional stats? (Y or N)\n')
        see_additional_stats = input().upper()
    if see_additional_stats == 'Y':
        show_additional_stats(user)

    getaway_challenge = getaway(user)
    user_result = getaway_challenge.run()
    if user_result == 'failure':
        death()
        typeWriter('\n\nThanks for playing!')
        typeWriter('\n\nPress Y to play again\n')
        playagain = input().upper()
        if playagain == 'Y':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            main()
    else:

        chosen_path = choosePath(user)
        user_result = ''
        if chosen_path == 'A':
            typeWriter('\nYou have been teleported to the Sky Kingdom')
            typeWriter('\n\n  The Virtual World is Generating')
            
            typeWriter('...\n\n', lag = 0.5)
            world = SkyKingdom(user)
            user_result = world.run()
        elif chosen_path == 'B':
            typeWriter('\nYou have been teleported to The Underworld')
            typeWriter('\n\n  The Virtual World is Generating')
            typeWriter('...\n\n', lag=0.5)
            world = Underworld(user)
            user_result = world.run()

        # failure or final boss battle
        if user_result == 'failure':
            death()
            typeWriter('\n\nThanks for playing!')
            typeWriter('\n\nPlay again? (Y or N)\n')
            playagain = input().upper()
            if playagain == 'Y':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                main()

        # final boss battle
        else:
            typeWriter('\n\nYou activate the gem to return home')
            typeWriter('..\n\n', lag=0.5)
            typeWriter('What??? \nInstead of returning home, you are teleported to a strange'
                       ' arena. \nLights flash on and you are ushered into the middle.'
                       '\n\n"The next challenger is ')
            typeWriter(user.returnName(), user = user)
            typeWriter('! Let\'s see if he has what it takes to defeat the Grandmaster!"\n\n')
            
            
            # user can fight the boss as many times as he/she wants
            #nested loops
            while True:
                # run the final battle method
                final_battle = FinalBoss(user)
                user_result = final_battle.run()
                #writing results to file
                with open("Results.txt","a") as t:
                    t.write("\n"+user.returnName()+"  "+user_result.upper())
                    
                # if user dies
                if user_result=="failure":
                    playagain = ''
                    # will user play again?
                    while playagain != 'Y' and playagain != 'N':
                        typeWriter('\n\nFight the Boss again? (Y or N)\n')
                        playagain = input().upper()
                    # user wants to play again; easter egg here (if user enters a number they get that many lives)
                    if playagain == 'Y':
                        typeWriter('You get ready to battle. What\'s your battle cry? ')
                        easter_egg = input()
                        # try making user input into an int, if so easter egg! if not, continue w two lives
                        #try except block
                        try:
                            val = int(easter_egg)
                            if 0 < val < 11:
                                user.resetLives(val)
                                typeWriter('Congrats! You\'ve just gained ' + easter_egg + ' lives!\n\n')
                            else:
                                typeWriter('Time to fight the Grandmaster again!')
                                user.resetLives(2)
                        except:
                            typeWriter('\nYou shout "' + easter_egg + '" as you enter the arena.\n')
                            typeWriter('Time to fight the Grandmaster again!')
                            user.resetLives(2)
                    elif playagain == 'N':
                        break
                elif user_result == 'success':
                    win()
                    break


main()
