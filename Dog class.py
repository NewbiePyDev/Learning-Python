from time import sleep

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll(self):
        print(self.name.title() + " rolled over!")

    def run(self):
        print(self.name.title()+" is running!")

    def call(self):
        print(self.name.title()+" came back...")

    def feed(self):
        print("You've fed "+ self.name + ".")

    def sleep(self):
        print(self.name + " is sleeping...")


my_dog = Dog('Sweetie', 6)
your_dog = Dog('Bark', 4)

class Human:
    def __init__(self, name):
        self.name = name
    def run(self):
        print(self.name + " is running after her dog " + your_dog.name.title()+"!")
        

human = Human('Haley')

human.run()

my_dog.run()
sleep(0.5)
my_dog.feed()
sleep(0.5)
my_dog.sleep()
sleep(0.5)
my_dog.roll()
