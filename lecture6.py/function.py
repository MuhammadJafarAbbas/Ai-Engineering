# def avg(a,b,c):
#     return(a+b+c)/3


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print(avg(a,b,c))

# def sum(a=5,b=7):
#     return a*b

# print(sum())



# def find(a):
#     idx=0
#     list=[1,2,5,7,8,4]
#     for i in list:
#         if i==a:
#             print(idx)
#             print("Found")
#             break
#         idx+=1
#     else:
#         print("Not found")


# find(4)

# def number(list):
#     print("The list is: ",list)


# number([6,2,4,6,8])

# def fac(a):
#     if(a==0):
#         return 1
#     else:
#         return a*fac(a-1)

# print(fac(5))
    
# def fac(a):
#     if(a==0):
#         return 1
#     else:
#         for i in range(1,a+1):
#             a=a*i
#             return a

# print(fac(5))

# def exchange(rup):
#     usd=300
#     return usd*rup

# print(exchange(5))

# def func(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "Odd"


# print(func(5))

# def sum(n):
#     if(n==0):
#         return 0
#     print(n)
#     return n + sum(n-1)

# print(sum(5))

def print_list(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list([1, 2, 3, 4, 5])