from termcolor import *
import time
import random
import config

class FinalBoss(object):

    def __init__(self, user):
        self.user = user

    def colorize(self, text, color='red'):
        text = colored(text, color, attrs=['bold'])
        return text

    def typeWriter(self, text, isColored=False, lag=config.lag, color='red'):
        text = list(str(text))
        if isColored:
            for letter in text:
                time.sleep(lag)
                print(self.colorize(letter, color), end='', flush=True,)
        else:
            for letter in text:
                time.sleep(lag)
                print(letter, end='', flush=True)

    def dodge(self):
        self.typeWriter('\nHe swipes at you, what direction do you want to dodge?', isColored=True)
        self.typeWriter('\n\nA) Duck Right. \nB) Roll Left. \nC) Stand your ground. He is expecting you to dodge.\n')
        while True:
            user_choice = input().upper()
            if user_choice == 'A' or user_choice == 'B' or user_choice == 'C':
                break
            else:
                self.typeWriter('Try typing something valid.\n')

        directions=["A", "B", "C"]
        attackdirection=random.randint(0, 2)
        dodge=False
        if directions.index(user_choice)==attackdirection:
            dodge=True

        return dodge

    def grandmaster_damage(self, grandmaster_health, damage):
        grandmaster_health -= damage
        self.typeWriter('\nThe Grandmaster has taken ' + str(damage) + ' damage\n', isColored=True)
        if grandmaster_health>60:
            self.typeWriter("You've barely made a dent, he smiles and charges at you again. ")

        elif grandmaster_health>30:
            self.typeWriter("\nHis actions seem to be slowing as various wounds on his body bleed out. \nYou must keep "
                            "fighting. He charges, no longer having that smirk on his face. ")

        elif grandmaster_health>0:
            self.typeWriter("\nHe seems as if he is about to faint, but he picks himself back up. He looks at you with "
                            "a deathly glare. \nThe world around you is fading closer to reality and freedom is within "
                            "reach \n", isColored=True)

        return grandmaster_health

    def attack(self, grandmaster_health):
        self.typeWriter('\nHe appears to be tired as he lays down after his last swipe. This is your chance to attack!'
                        ' Where do you attack him?\n', isColored=True)
        self.typeWriter('\n\nA) Arms \nB) Legs \nC) Chest\n\n')
        while True:
            user_choice = input().upper()
            if user_choice == 'A' or user_choice == 'B' or user_choice == 'C':
                break
            else:
                self.typeWriter('Try typing something valid.\n')

        directions = ["A", "B", "C"]
        weakness = random.randint(0, 2)

        if directions.index(user_choice) == weakness:
            damage=(float(self.user.returnDamage())*3)
            self.typeWriter('\nThe Grandmaster stumbles and stares at you in confusion, wondering how you knew that was '
                            'his current weakness\n', isColored=True)
            grandmaster_health=self.grandmaster_damage(grandmaster_health, damage)

        else:
            damage = (float(self.user.returnDamage()))
            self.typeWriter('\nThe Grandmaster grins and gets to his feet as you charge. Side stepping his next attack'
                            ', you hesitate and barely graze him.\n')
            grandmaster_health=self.grandmaster_damage(grandmaster_health, damage)

        return grandmaster_health

    def death(self):
        self.typeWriter('\nYou\'ll never make it back to reality and you are out of lives.'
                        ' You stumble around as the world starts to fade to black...')

    def takedamage(self):
        damage=random.randint(0,30)
        self.typeWriter('You take ' + str(damage) + ' damage.\n')
        lifelost=self.user.losehealth(damage)
        self.typeWriter('Health remaining: ')
        self.typeWriter(self.user.returnChangingHealth())
        print()
        if lifelost:
            self.typeWriter('\nLives left: ')
            self.typeWriter(self.user.returnLives(), color=self.user.returnColor())
            print()

    def grandmasterdeath(self):
        self.typeWriter('\nThe Grandmaster stumbles, frantically scrambling to find something to hold him up as he falls.\nThis is it. You dash for him,' 
                        ' delivering one last blow, and watch him fall.', isColored=True)

    def battle(self):
        self.typeWriter('The Grandmaster swipes at you and you dodge at the last second.\n', isColored=True)
        self.typeWriter('You know that it was just a warning attack, the rest will not be so easy.\n')
        grandmaster_health=100
        while self.user.returnLives()!=0:
            dodge=self.dodge()
            if not dodge:
                self.takedamage()
                self.typeWriter("\nHe knew where to attack too well, he hits you and you are knocked to your feet, but"
                                " you keep looking for an opening\n")
            if dodge:
                self.typeWriter('\nAlmost as if you could read his mind, you avoid his attack and look for an opening. \n')
            opening=False
            if random.randint(1,2)==2: opening=True
            if opening:
                grandmaster_health = self.attack(grandmaster_health)
            else:
                self.typeWriter('\nYou must bide your time, there is no opening in sight, death looks you in the face as '
                                'he charges you again.\n')
            if grandmaster_health<=0:
                self.grandmasterdeath()
                result = "success"
                return result

            if self.user.returnLives() == 0:
                self.death()
                result="failure"
                return result

    def run(self):
        self.typeWriter('\n\nAs you look around, you can see the fabric of reality and the game almost mixing.\n', isColored=True)
        self.typeWriter('This is your path to escape and you know it.\n')

        self.typeWriter('\nA huge laugh fills the room, and the Grandmaster looks you dead in the eyes with a cold '
                        'expression on his face.\n\n')
        self.typeWriter('You never should have come to my realm, this will be the end of you!\n\n', isColored=True)

        result=self.battle()

        return result

