class User(object):

    def __init__(self, name, choice, lives = 2, damage = 100, range = 100, stealth = 100):

        self.lives = lives
        self.name = name

        if choice == 'A':
            self.type = 'Ranger'
            self.color = 'green'
            self.weapon = 'crossbow'
            self.damage = 30
            self.range = 90
            self.stealth = 60
        elif choice == 'B':
            self.type = 'Sorcerer'
            self.color = 'yellow'
            self.weapon = 'magic staff'
            self.damage = 90
            self.range = 60
            self.stealth = 30
        else:
            self.type = 'Assassin'
            self.color = 'magenta'
            self.weapon = 'poison dagger'
            self.damage = 60
            self.range = 30
            self.stealth = 90

    def returnName(self):
        return self.name

    def returnType(self):
        return self.type

    def returnColor(self):
        return self.color

    def returnWeapon(self):
        return self.weapon

    def returnDamage(self):
        return self.damage

    def returnRange(self):
        return self.range

    def returnStealth(self):
        return self.stealth

    def returnLives(self):
        return self.lives

    def loseLife(self, lostLife = True):
        if lostLife:
            self.lives -= 1

    def gainLife(self, gainLife = True):
        if gainLife:
            self.lives += 1
