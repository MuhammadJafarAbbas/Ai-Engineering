# #blueprint
# class Car:
#     name="Toyota Corolla"
#     brand="Grande 1.8"

# #object
# car1=Car()
# print(car1.name)
# print(car1.brand)

# class Student:
#     name="Salah"

# student1=Student()
# print(student1.name)

#constructor
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks


# s1=Student("Salah",89)
# print(s1.name)
# print(s1.marks)

# s2=Student("naeem",79)
# print(s2.name)
# print(s2.marks)


# class Car:
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand

# c1=Car("Toyota Corolla","Grande 1.8")
# c2=Car("Changan Alsvin","1.5L")

# print("Car 1 name:",c1.name)
# print("Car 1 brand:",c1.brand)

# print("Car 2 name:",c2.name)
# print("Car 2 brand:",c2.brand)

# class Car:
#     name="Fav Cars"
#     def __init__(self,name,brand):
#         self.name=name
#         self.brand=brand

# c1=Car("Toyota Corolla","Grande 1.8")
# c2=Car("Changan Alsvin","1.5L")

# print("Car 1 name:",c1.name)
# print("Car 1 brand:",c1.brand)

# print("Car 2 name:",c2.name)
# print("Car 2 brand:",c2.brand)
# print(Car.name)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val

#         print("Averege marks of",self.name,"is",sum/len(self.marks))

# student1=student("Salah",[89,67,65])
# student1.get_avg()

# 

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     @staticmethod
#     def hello():
#         print("hello world")

#     def getRec(self):
#         sum=0
#         idx=0
#         while idx<len(self.marks):
#             sum+=self.marks[idx]
#             idx+=1
            
#         print("Name:",self.name,"get marks:",sum/len(self.marks))

# s1=student("Fazal",[67,89,76,99])

# s1.hello()
# s1.getRec()
    
class Account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance

    def debit(self,amount):
        if(amount<=self.balance):
            self.balance=self.balance-amount
            print(amount,"is deducted from your account your current balance is:",self.balance)

    def credit(self,amount):
        self.balance+=amount
        print(amount,"is added to your account")
        print("current balance is:",self.balance)



b1=Account(1122,2000)

b1.debit(1200)
b1.credit(300)

    

        


        