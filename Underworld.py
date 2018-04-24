from User import User
from termcolor import *
import time

class Underworld(object):

    def __init__(self, user):
        self.user = user


    def colorize(self, text, color = 'red'):
        text = colored(text, color, attrs=['bold'])
        return text

    def typeWriter(self, text, isColored=True, lag=0.02, color = 'red'):
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
        self.typeWriter('Welcome to the Underworld', isColored=True) # greetings
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

        self.typeWriter('\n\nYou sneak into the castle of Death, but you see a Demon King '
                        'standing guard and hungry. What do you do? ')

        self.typeWriter('\n\nA) Attempt close combat. \nB) Attempt ranged attack. \nC) Sneak past him.\n\n',isColored=False)
        while True:
            user_choice = input()
            if user_choice == 'A' or user_choice == 'B' or user_choice == 'C':
                break
            else:
                self.typeWriter('Try typing something valid.\n')

        if user_choice == 'A':
            if self.user.returnDamage() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou defeated the Demon King!!')
                battle_one_result = True
                return battle_one_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your damage is ')
                self.typeWriter(self.user.returnDamage(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to defeat the Demon King. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_one_result

        if user_choice == 'B':
            if self.user.returnRange() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou defeated the Demon King!!')
                battle_one_result = True
                return battle_one_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your range is ')
                self.typeWriter(self.user.returnRange(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to defeat the Demon King. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_one_result

        if user_choice == 'C':
            if self.user.returnStealth() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou snuck past the Demon King!!')
                battle_one_result = True
                return battle_one_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your stealth is ')
                self.typeWriter(self.user.returnStealth(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to sneak past the Demon King. '
                                '\n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_one_result

    def battleTwo(self):

        battle_two_result = False #True = success, false = failure

        self.typeWriter('\n\nYou wander around and finally, you see the Father of all Demons and the'
                        'King of the Underworld on his throne'
                        ' with his mightiest children around him. '
                        '\nIt is rumored that the heart of King of all Demons, Hydra, is a special gem which will '
                        'allow people to return back to the world.\n'
                        'You know the king is destructive and merciless, '
                        'and he rules the world with his Bubble Horns. What would you do? ')

        self.typeWriter('\n\nA) Destroy his army. \nB) Send in your dogs to '
                        'distract them while you ambush from the back. \nC) Kill and take his heart.\n\n',isColored=False)
        while True:
            user_choice = input()
            if user_choice == 'A' or user_choice == 'B' or user_choice == 'C':
                break
            else:
                self.typeWriter('Try typing something valid.\n')

        if user_choice == 'A':
            if self.user.returnDamage() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou defeated the Demon King!!!. You now have the magical Gem')
                battle_two_result = True
                return battle_two_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your damage is ')
                self.typeWriter(self.user.returnDamage(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to defeat the Demon King and his children.'
                                ' The King rips your finger off. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_two_result

        if user_choice == 'B':
            if self.user.returnRange() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou have successfully ambushed the King!!!. '
                                'You now have the magical Gem')
                battle_two_result = True
                return battle_two_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(),color=self.user.returnColor())
                self.typeWriter(', your range is ')
                self.typeWriter(self.user.returnRange(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to ambush the Demon King and his children.'
                                'You lost your toenail. \n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_two_result

        if user_choice == 'C':
            if self.user.returnStealth() >= 60:
                self.typeWriter('\nGreat Choice, ')
                self.typeWriter(self.user.returnType() + ' ' + self.user.returnName(), color=self.user.returnColor())
                self.typeWriter('\nYou have killed Hydra and stole his heart!')
                battle_two_result = True
                return battle_two_result
            else:
                self.typeWriter('\nAs a ')
                self.typeWriter(self.user.returnType(), color=self.user.returnColor())
                self.typeWriter(', your stealth is ')
                self.typeWriter(self.user.returnStealth(), color=self.user.returnColor())
                self.typeWriter(', which wasn\'t enough to sneak up to the Demon King. '
                                'You and your friends got captured.\n\nYou have lost a life!')

                self.user.loseLife()
                self.typeWriter('\nLives left: ')
                self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
                return battle_two_result

    def death(self):
        self.typeWriter('\n\n You\'ll never make it back to reality and you are out of lives.'
                        'You stumble around as the world starts to fade to black...')

    def discoverGem(self, battle_two_result):
        if battle_two_result:
            self.typeWriter('\n\nCongrats child, you have collected the magical gem and completed'
                            ' the Underworld quest!!!\n')
        else:
            self.typeWriter('\n\nWhile in the King\'s captivity, you regret your actions and ask to speak to'
                            ' the King. However, as merciless and destructive as he is, he decides to kill'
                            ' you on the spot and devours your body and your friends\'', lag=0.02)

