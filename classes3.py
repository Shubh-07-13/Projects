class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return (f"{self.name} sings song")
Jimmy = parrot("Jimmy", 4)
print(Jimmy.sing("The Nights"))
