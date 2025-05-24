# # simple inheritance

# ## Base Class
# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} is make a sound")

# ## child/ derived class
# class Dog(Animal):

#     # def __init__(self):
#     #     self.behaviour = "Funny"

#     def speak(self): # this method overrides the base class method
#         print(f"{self.name} is barking.")
#         # print(f"{self.name} is barking. He is Very {self.behaviour}") # this constructor overloading

# #to call base class
# # gen = Animal("Generic Animal")
# # gen.speak()

# # to call derived class
# dog = Dog("bucky")
# dog.speak() # is using inherited speak method
# # dog.speak1() # is using his won speak1 method

## ------  Super Keyword

## Base Class
class Animal:
    def __init__(self):
        self.name = "Bucky"
    
    def speak(self):
        print(f"{self.name} is make a sound")

## child/ derived class
class Dog(Animal):

    def __init__(self,breed):
        super().__init__() # self.name is not be used without super() in constructor
        self.breed = breed

    def speak(self): # this method overrides the base class method
        super().speak() # accessing speak() from parent and child
        print(f"{self.name} is barking. He is {self.breed}")  # self.name is not be used without super() in constructor

dog = Dog("Golden Retriver")
dog.speak()