class User(object):

    def __init__(self, name, choice, lives = 2, damage = 100, range = 100, stealth = 100):

        self.lives = lives
        self.name = name

        if choice == 'A':
            self.type = 'Archer'
            self.color = 'red'
            self.weapon = 'bow and arrow'
            self.damage = 30
            self.range = 90
            self.stealth = 60
            self.health = 60
            self.changinghealth= 60

        elif choice == 'B':
            self.type = 'Sorcerer'
            self.color = 'yellow'
            self.weapon = 'magic staff'
            self.damage = 90
            self.range = 60
            self.stealth = 30
            self.health = 40
            self.changinghealth = 40
        else:
            self.type = 'Assassin'
            self.color = 'magenta'
            self.weapon = 'poison dagger'
            self.damage = 60
            self.range = 30
            self.stealth = 90
            self.health = 50
            self.changinghealth = 50
    def returnName(self):
        return self.name

    def returnHealth(self):
        return self.health

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

    def returnChangingHealth(self):
        return self.changinghealth

    def loseLife(self, lostLife = True):
        if lostLife:
            self.lives -= 1

    def gainLife(self, gainLife = True):
        if gainLife:
            self.lives += 1

    def losehealth(self, damage):
        self.changinghealth -= damage
        if self.changinghealth>0:
            lifelost=False
            return lifelost
        else:
            lifelost=True
            self.loseLife()
            self.changinghealth=self.health
            return lifelost

    def resetLives(self, lives):
        self.lives = lives
