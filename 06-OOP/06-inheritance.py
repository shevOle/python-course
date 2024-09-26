class Animal:
    def __init__(self, age):
        self.age = age
        print('Animal is created')

    def is_old(self):
       if self.age < 5:
          return print('I\'m not old yet')
       return print('I\'m a bit old now')

    def eat(self):
        print('omnomnom')

    def poke__with_stick(self):
        print('HEY!!!!!!!! I\'m alive, stop it!!!')

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        
        self.name = name
        print('Dog is created')

    def eat(self):
        print('*eating dog food and wagging it\'s tale')

    def speak(self):
        print('woof!')


a_dog = Dog('Gabriel', 3)

print()
# inherited method
a_dog.is_old()

# overwritten method
a_dog.eat()

# method of the derived class
a_dog.speak()

# inherited method
a_dog.poke__with_stick()