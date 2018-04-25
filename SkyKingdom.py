from User import User
from termcolor import *
import time
import config


class SkyKingdom(object):

    def __init__(self, user):
        self.user = user


    def colorize(self, text, color = 'blue'):
        text = colored(text, color, attrs=['bold'])
        return text

    def typeWriter(self, text, isColored=True, lag=config.lag, color = 'blue'):
        text = list(str(text))
        if isColored:
            for letter in text:
                time.sleep(lag)
                print(self.colorize(letter, color), end='', flush=True)
        else:
            for letter in text:
                time.sleep(lag)
                print(letter, end='', flush=True)

    def run(self):
        self.typeWriter('Welcome to Sky Kingdom', isColored=True) # greetings
        self.battleOne()
        battle_two_result = self.battleTwo()
        if self.user.returnLives() == 0:
            self.death()
            result = 'failure'
        else:
            self.discoverGem(battle_two_result)
            result = 'success'

        return result

    def battleOne(self):

        battle_one_result = False #True = success, false = failure

        self.typeWriter('\n\nYou sneak into the castle, but you see a knight '
                        'standing guard. What do you do? ')

        self.typeWriter('\n\nA) Attempt close combat \nB) Attempt ranged attack. \nC) Sneak past him.\n\n',isColored=False)
        while True:
            user_choice = input().upper()
            if user_choice == 'A' or user_choice == 'B' or user_choice == 'C':
                break
            else:
                self.typeWriter('Try typing something valid.\n')

        if user_choice == 'A':
            if self.user.returnDamage() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou defeated the knight!!')
                battle_one_result = True
                return battle_one_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your damage is ')
                self.typeWriter(self.user.returnDamage(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to defeat the knight. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_one_result

        if user_choice == 'B':
            if self.user.returnRange() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou defeated the knight!!')
                battle_one_result = True
                return battle_one_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your range is ')
                self.typeWriter(self.user.returnRange(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to defeat the knight. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_one_result

        if user_choice == 'C':
            if self.user.returnStealth() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou snuck past the knight!!')
                battle_one_result = True
                return battle_one_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your stealth is ')
                self.typeWriter(self.user.returnStealth(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to sneak past the knight. '
                                'He discovers you.\n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_one_result

    def battleTwo(self):

        battle_two_result = False #True = success, false = failure

        self.typeWriter('\n\nYou wander around and finally, you see the king of Sky Kingdom on his throne '
                        'with his soldiers around him. '
                        '\nIt is rumored that the King holds a special gem which will '
                        'allow people to transcend the world.\n'
                        'You know the king is kind, but he rules with an iron fist. What should you do? ')

        self.typeWriter('\n\nA) Fight the troops. \nB) Send in your friend to '
                        'distract them while you ambush from the window. \nC) Steal the gem.\n\n',isColored=False)
        while True:
            user_choice = input().upper()
            if user_choice == 'A' or user_choice == 'B' or user_choice == 'C':
                break
            else:
                self.typeWriter('Try typing something valid.\n')

        if user_choice == 'A':
            if self.user.returnDamage() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou defeated the King! You have free reign to look around for the gem.')
                battle_two_result = True
                return battle_two_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your damage is ')
                self.typeWriter(self.user.returnDamage(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to defeat the king and his troops.'
                                ' The King captures you. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_two_result

        if user_choice == 'B':
            if self.user.returnRange() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou have successfully ambushed the king and his troops. '
                                'You force him to hand over the gem!')
                battle_two_result = True
                return battle_two_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your range is ')
                self.typeWriter(self.user.returnRange(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to ambush the King and his troops.'
                                'You and you friend get captured. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_two_result

        if user_choice == 'C':
            if self.user.returnStealth() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou have successfully stolen the gem!! Time to go back!')
                battle_two_result = True
                return battle_two_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(), color=self.user.returnColor())
                self.typeWriter(', your stealth is ')
                self.typeWriter(self.user.returnStealth(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to sneak past the King and his troops and '
                                'steal the gem. The King captures you.\n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_two_result

    def death(self):
        self.typeWriter('\n\n You\'ll never make it back to reality and you are out of lives.'
                        'You stumble around as the world starts to fade to black...')

    def discoverGem(self, battle_two_result):
        if battle_two_result:
            self.typeWriter('\n\nCongrats, you have collected the gem and beat the Sky Kingdom quest!!\n')
        else:
            self.typeWriter('\n\nWhile in the King\'s captivity, you regret your actions and ask to speak to'
                            ' the King. You explain your situation to him. \nSurprisingly, the King breaks down '
                            'in tears. He is also in the same situation as you, but he grew attached'
                            '\nto the people here so he never left. He understands your pain and offers to forgive you'
                            ' and give you the gem.\n'
                            'Congrats, you have collected the gem and beat the Sky Kingdom quest!!\n')

# main test function
'''def main():
    user = User('Bobby', 'B')
    world = SkyKingdom(user)
    world.run()
main()'''
