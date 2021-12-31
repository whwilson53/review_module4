class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def bark(self):
        return self.sound + ' ' + self.sound

first_dog = Dog('Fido', 'brown', 'woof!')
print(first_dog.name)
print(first_dog.color)
first_dog.bark()

second_dog = Dog('Lady', 'blonde', 'arf!')
print(second_dog.sound)