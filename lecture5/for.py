# num={1,2,5,4,7,8,4,2,12}
# for el in num:
#     print(el)

# tup=(7,2,4,6,8,10,15,22,24,27,89,21)
# found=False
# x=int(input("Enter the number to search:"))
# idx=0
# for el in tup:
#     if el==x:
#         found=True
#         print(idx)
#     idx+=1
 

# if(found==True):
#     print("The number is found in the tuple")
# else:
#     print("The number is not found in the tuple")


#range 

# for i in range(10): #range(stop)
#     print(i)

# for i in range(1,10): #range(start,stop)
#     print(i)

# for i in range(1,10,2): #range(start,stop,step)
#     print(i)

# for i in range(1,100,2): #range(start,stop,step)
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i*5)

# i=1
# n=0
# while(i<=10):
#     n+=i
#     i+=1
# print("The sum of first 10 natural numbers is:",n)

fac=1
for i in range(1,6):
    fac*=i
print("The factorial of 5 is:",fac)