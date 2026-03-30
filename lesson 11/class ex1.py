# In this exercise, your task is to practice inheritance by creating game character classes inspired by the Super Mario world! Wahhooo!
#
# First, create a base class called Character.
# A character should have a name and a method called introduce() that prints the character’s name.
#
# After that, create a class called MarioCharacter that inherits from Character.
# In addition to the inherited properties, this class should have a lives attribute.
# It should also have a method called jump() that prints that the character jumps.
#
# Then create a class called FireMario that inherits from MarioCharacter.
# This class should have one extra method called throw_fireball() that prints that the character throws a fireball.
#
# In the main program, create one normal Mario character and one Fire Mario character.
# Call their methods to show how inheritance works.
# Make sure that the child/subclasses can use both their own methods and the methods inherited from the parent classes.

class Character:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print(f"It's-a-mee {self.name}")

class MarioCharacter(Character):
    def __init__(self,name, lives):
        super().__init__(name)
        self.lives = lives

    def jump(self):
        print(f"{self.name}Jumps---boing")

class FireMario(MarioCharacter):
  

    def throw_fireball(self):
        print(f"{self.name} throws a fireball")


mario=MarioCharacter("Mario",3)
mario.introduce()
mario.jump()

fire_mario=FireMario("Fire Mario", 5)
fire_mario.introduce()      # Ereditato da Character (tramite MarioCharacter)
fire_mario.jump()           # Ereditato da MarioCharacter
fire_mario.throw_fireball() # Definito in FireMario
print(f"Lives: {fire_mario.lives}")


