 #function-->def functionname(a,b):


# write a progam which will take input from user a no. is even it will calculate even factorial and it willodd factorial if the number is odd
# def factors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end="")
#return 10
# x = factors(12)
#print(x)
#----------x-----------x--------x--------x-----


# def even_fact(n):
#     ans=1
# def odd_fact(n):
#     pass
# n = int (input("enter a number : "))
# if n%2==0:
#     print(even_fact(n))
# else:
#     print(odd_fact(n))
# for i in range(2,n+1,2):
#     ans *=i
#     return ans
# def odd_fact(n):
#     ans=1
#     for i in range (1,n+1,2):
#         ans*=i
#         return ans
    



    #-----------xx-----x----x---x----x-----x-----x----x---x---x---x---x--x--c----x--x--




    # list=[1,2,3,"hello",5.7]
    # #print(list)
    # for i in range(len(list)):
    #     print(list[i],end="")



    # lst=eval(input("enter the list: "))
    # print(lst)
    # print(type(lst))
    # w.a.p.    which take input from and increase all the even no. by 5 and decrease all all odd on.

lst=eval(input("enter the list"))
print(lst)
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]+=5
    else:
        lst[i]-=5
        print(lst)