# i=1
# while i<=100:
#     print(i)
#     i=i+1


# i=100
# while i>=1:
#     print(i)
#     i-=1

# i=1
# while i<=10:
#     print("5 table",i*5)
#     i+=1

tuple=(12,3,4,43,56,42,6,7,48,99,87,33)
idx=0
found=False
x=34
while idx<len(tuple):
    if tuple[idx]==x:
        found=True
        break
    idx+=1

if(found==True):
    print("found",x)
else:
    print("not found",x)