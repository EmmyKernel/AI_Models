class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('Bone is ready')
        return "Eating food"

    
class Dog(Animal):
    def bark(self):
        self.eat()
        print(f'My name is {self.name}')
        return "woof"

    
my_dog = Dog("Puppy")

print(my_dog.bark())
print(my_dog.eat())

