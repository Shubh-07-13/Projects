class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
class Dog(Animal):
    def __init__(self, name, breed, habitat):
        super().__init__(name, breed)
        self.habitat = habitat
    def sound(self):
        return "arf! arf!"
class Parrot(Animal):
    def __init__(self, name, breed, phrase):
        super().__init__(name, breed)
        self.phrase = phrase
Mike = Dog("Mike", "Golden Doodle", "The House")
Pike = Parrot("Pike", "Parrot Breed", "Hello!")

print(Pike.phrase)
print(Mike.name)
print(Mike.habitat)
print(Mike.breed)
print(Mike.sound())