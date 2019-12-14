

class Dog:
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def speak(self):
        print("wof wof")


my_dog = Dog("hodor", "mestizo", 4)
my_dog2 = Dog("doggy", "bulldog", 2)
my_dog3 = Dog("tobby", "dalmata", 6)

print(my_dog2.age)