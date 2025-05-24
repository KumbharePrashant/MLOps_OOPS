## Single/ basic inheritance

# class Parent:
#     def __init__(self,name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello my name is {self.name}")

# ## child/ derived class
# class Child(Parent):

#     def Play(self): 

#         print(f"{self.name} is playing")  # self.name is not be used without super() in constructor

# child = Child("Alice")
# child.greet()
# child.Play()

# ------------------------------------

## Multilevel Inheritance
# base class
# class Grandparent:
#     def __init__(self,name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} is telling story")

# # intermediate class 
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working")

# ## derived class
# class Child(Parent):

#     def Play(self): 
#         print(f"{self.name} is playing")  # self.name is not be used without super() in constructor

# child = Child("Alice")
# child.tell_story()
# child.work()
# child.Play()

# --------------------------------------------

# Heirarchical Inheritance
# class Parent():
#     def __init__(self,name):
#         self.name = name

#     def Greet(self):
#         print(f"Hello my name is {self.name}")

# ## derived class
# class Child1(Parent):

#     def Work(self): 
#         print(f"{self.name} is working")  # self.name is not be used without super() in constructor

# ## derived class
# class Child2(Parent):

#     def Play(self): 
#         print(f"{self.name} is playing")

# child1 = Child1("Alice")
# child2 = Child2("Bruce")

# child1.Greet()
# child1.Work()
# child2.Greet()
# child2.Play()

# --------------------

class A:
    def __init__(self,name):
        self.name = name
    def Greet(self):
        print(f"Hello from A,{self.name}")
class B(A):
    
    def Greet(self):
        print(f"Hello from B,{self.name}")
        super().Greet()
class C(A):
    
    def Greet(self):
        print(f"Hello from C,{self.name}")
        super().Greet()
class D(B,C):
    
    def Greet(self):
        print(f"Hello from D,{self.name}")
        super().Greet()

d = D("Frank")
d.Greet()

# -------------------------------

# Hybrid inheritance (animal, mammle(animal), bird(animal), bat(mammle, bird)