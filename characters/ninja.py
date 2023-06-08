class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = [pet_food, 3]
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"{self.first_name} {self.last_name} takes {self.pet.name} on a walk.")
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        self.pet_food[1] -= 1
        if self.pet_food[1] > 0:
            print(f"{self.first_name} {self.last_name} feeds {self.pet_food[0]} to {self.pet.name}! Only {self.pet_food[1]} {self.pet_food[0]} left!")
            return self
        else:
            print(f"{self.first_name} {self.last_name} has no more pet food!")
            return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} {self.last_name} tries to give {self.pet.name} a bath.")
        self.pet.noise()
        return self
