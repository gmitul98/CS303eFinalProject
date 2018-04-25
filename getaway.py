from User import User
from termcolor import *
import time, random
import config

class getaway(object):

    def __init__(self, user):
        self.user = user

    def colorize(self, text, color = 'green'):
        text = colored(text, color, attrs=['bold'])
        return text

    def typeWriter(self, text, isColored=True, lag=config.lag, color = 'green'):
        text = list(str(text))
        if isColored:
            for letter in text:
                time.sleep(lag)
                print(self.colorize(letter, color), end='', flush=True)
        else:
            for letter in text:
                time.sleep(lag)
                print(letter, end='', flush=True)

    def monsterGraphic(self):
        print('\n\n')
        print('\,__   __, /                                     ')
        print(' \   \/  ./                                      ')
        print('  \      /                                       ')
        print('   \    /      ,-----------"--,                  ')
        print('    |   \____/             /-\                   ')
        print('     \                    | .O  `\       !!!     ')
        print('      |          ,--     |\_______)       o,     ')
        print('       |       <|   ,     "/ / / /       </      ')
        print('        `,      |~~~|     / / / /  (-----/------)')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@~~~~~~~~')

    def row1(self,a,b):
        print('\n\n\n\n', a + '         o,       \n', end='', flush=True)
        print(a +             '         </      \n', end='', flush=True)
        print(a +             '   (-----/------)\n', end='', flush=True)
        print(b +             '~~~~~~~~@~~~~~~~~~~')

    def row2(self, a, b):
        print('\n\n\n\n', a + '      o_/|      \n', end='', flush=True)
        print(a +             '       [\_|      \n', end='', flush=True)
        print(a +             '   (------|-----)\n', end='', flush=True)
        print(b +             '~~~~~~~~~~@~~~~~~~~')

    def run(self):

        self.typeWriter('\n\nYou walk around and see a canoe in a river.'
                        '\nHmm. You notice that '
                        'you are on an island, but you see the mainland far away'
                        '.\nYou climb onto the canoe and begin rowing towards the mainland.', isColored=True)
        self.typeWriter('\nYou row\nand row\nand row...')
        self.typeWriter('\n\nOh no!\nSKREEK! You hear the deathly shriek of a weird, giant fish monster.'
                        'Quick, row faster! It\'s chasing after you!', isColored=True)
        user_result = self.rowGame()

        return user_result

    def rowGame(self):
        a = ''
        b = ''
        #counter = 0
        self.typeWriter('\nYou are tired, but you must make sure you keep rowing or else the creature will catch you!'
                        '\nYou don\'t know when your arms will give out, but when you do,'
                        '\nmake sure to Press ENTER to keep rowing!! \nIf you don\'t click fast enough,'
                        ' the creature will catch you.')
        while True:
            self.typeWriter('\n\nWhat difficulty would you like?\n\nA) Easy\nB) Medium\nC) Hard\nD) Insane\n', isColored=False)
            user_difficulty = input('\n').upper()
            if user_difficulty == 'A' or user_difficulty == 'B' or user_difficulty == 'C' or user_difficulty == 'D':
                break
        if user_difficulty == 'A':
            difficulty = 1
            self.typeWriter('You\'ve chosen Easy!')
        elif user_difficulty == 'B':
            difficulty = 0.8
            self.typeWriter('You\'ve chosen Medium!')
        elif user_difficulty == 'C':
            difficulty = 0.6
            self.typeWriter('You\'ve chosen Hard!')
        else:
            difficulty = 0.49
            self.typeWriter('You\'ve chosen Insane!')

        while True:
            user = input(self.colorize('\nOkay!! Press ENTER to begin playing!\n'))
            if user.upper() == "":
                break
        start_time = time.time()
        counter = 0

        while True:
            print('\n\n\n\n\n\n\n')
            #time.sleep(0.5)
            if counter % 2 == 0:
                self.row1(a, b)
            else:
                self.row2(a, b)
            time.sleep(0.35)
            a += '       '
            b += '~~~~~~~'
            counter+=1
            if counter%20 == 0:
                a = ''
                b = ''
            if counter%(random.randint(3,9)) == 0:
                user_time = time.time()
                user_input = input()
                elapsed_time = time.time() - user_time
                #print(elapsed_time)
                time.sleep(0.2)
                if elapsed_time > difficulty:
                    self.monsterGraphic()
                    self.typeWriter('You were caught by the big fish!')
                    return 'failure'
            game_time = time.time() - start_time
            if game_time > 20.0:
                self.typeWriter('Congrats you got away!')
                return 'success'

# main test function
'''def main():
    user = User('Bobby', 'B')
    world = getaway(user)
    world.run()
main()'''
