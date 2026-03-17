class Dog:
    created = 0

    def __init__(self, name, birth_year,sound="woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created += 1
    def bark(self, times):
        for i in range (times):
            print (self.sound)
        return


dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "meaw meaw")
dog1.bark(2)
dog2.bark(3)

print (f"{dog1.name} was born in {dog1.birth_year}")
print (f"{dog2.name} was born in {dog2.birth_year}")

