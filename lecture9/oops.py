# class student:
#     def __init__(self,name):
#         self.name=name


# s1=student("Ali Khan")
# print(s1.name)

# del s1.name

# class Account:
#     def __init__(self,acc_no,password):
#         self.acc_no=acc_no
#         self.__password=password  #__ use double underscor to make some thing private

#         self.__password=12345
#         self.acc_no=1

#     def reset_pass(self):
#         print("Account No:",self.acc_no)
#         print("Password:",self.__password)

# a1=Account(1,12345)
# print(a1.acc_no)
# print(a1.reset_pass())

#inheritence

# class Animal:
#     def eat(self):
#         print("Animals Can Eat")

# class Humen(Animal):
#     def speak(self):
#         print("Humen can also eat so humen are .......")

# h1=Humen()
# print(h1.eat())
# print(h1.speak())

# class Car:
#     @staticmethod
#     def start():
#         print("car is started......")

#     @staticmethod
#     def stop():
#         print("car is stopped...")

# class Toyata(Car):
#     def __init__(self,name):
#         self.name=name

# c1=Toyata("Grande")

# print(c1.name)
# c1.start()
# c1.stop()


#multi-level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car is started......")

#     @staticmethod
#     def stop():
#         print("car is stopped...")

# class Toyata(Car):
#     def __init__(self,name):
#         self.name=name

# class Fortuner(Toyata):
#     def __init__(self,name, type):
#         super().__init__(name)
#         self.type=type

# c1=Fortuner("Fortuner","diesel")

# print(c1.name)
# print(c1.type)
# c1.start()
# c1.stop()

#multiple inheritance
# class A:
#     a="Welcome to class A"

# class B:
#     b="Welcome to class B"

# class C(A,B):
#     c="Welcome to class C"

# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)

# class Car:
#     def __init__(self,type):
#         self.type=type
    
#     @staticmethod
#     def start():
#         print("car is started......")

#     @staticmethod
#     def stop():
#         print("car is stopped...")

# class Toyata(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# c1=Toyata("Grande","Petrol")

# print(c1.name)
# c1.start()
# c1.stop()

# class Person:
#     name="Jafar Abbas"

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name


# p=Person()
# p.changeName("Ali")
# print(p.name)

class student:
    def __init__(self,chem,bio,math):
        self.chem=chem
        self.math=math
        self.bio=bio

    @property        
    def percentage(self):
        return (self.math+self.bio+self.chem)/3

s1=student(67,85,94)
print(s1.percentage)
s1.chem=56
print(s1.percentage)



