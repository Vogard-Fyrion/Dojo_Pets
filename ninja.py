class Pet():
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        if(self.energy > 75):
            self.energy += 100 - self.energy
            return f"{self.name} sleeps and regains {100 - self.energy} energy."
        else:
            self.energy += 25
            return f"{self.name} sleeps and regains 25 energy."

    def eat(self):
        if(self.health > 90 and self.energy > 95):
            self.health += 100 - self.health
            self.energy += 100 - self.energy
            return f"{self.name} eats recovering {100 - self.health} health and {100 - self.energy} energy."
        elif(self.health > 90 or self.energy > 95):
            if(self.health > 90):
                self.health += 100 -self.health
                self.energy += 5
                return f"{self.name} eats recovering {100 - self.health} health and 5 energy."
            else:
                self.health += 10
                self.energy += 100 - self.energy
                return f"{self.name} eats recovering 10 health and {100 - self.energy} energy."

    def play(self):
        if(self.health > 95):
            self.health += 100 - self.health
            return f"{self.name} plays recovering {100 - self.health} health."
        else:
            self.health += 5
            return f"{self.name} plays recovering 5 health."

    def noise(self):
        return f"{self.name} barks. 'Woof'"

pet = Pet("Annabelle", "pug", "rollover")


class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} takes {self.pet.name} for a walk and {self.pet.play()}")

    def feed(self):
        print(f"{self.first_name} feeds {self.pet.name} {self.pet_food} and {self.pet.eat()}")
    
    def bathe(self):
        print(f"{self.first_name} bathes {self.pet.name} and {self.pet.noise()}")


ninja = Ninja("Levi", "Boggs", "milkbone", "purina", pet)

ninja.walk()
ninja.feed()
ninja.bathe()