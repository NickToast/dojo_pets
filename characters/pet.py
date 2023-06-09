class Pet:
    
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, health=100, energy=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} goes RAHHHHHHHHH")