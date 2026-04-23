# # Write a python program to compute the difference between two lists.

#Sample Data:-
# color1=["red", "orange","green","blue","white"],
# color2=["black","yellow"."green","blue"]

# Expected output:- 
# color1-color2:-["white"0,"orange","red"]
# color2-color1:-["black","yellow"]

# color1=["red", "orange","green","blue","white"]
# color2= ["black","yellow","green","blue"]
# lst1=[]
# lst2=[]
# for i in color1:
#     if i not in color2:
#         lst1.append(i)

# for i in color2:
#     if i not in color1:
#         lst2.append(i)


# print(lst1)
# print(lst2)
# ['red', 'orange', 'white']
# ['black', 'yellow']
# # Write  a python program to pack consecutive duplicate of a given list of element into sublists.
# lst=[0, 0 , 1 ,2, 3, 4, 4, 5, 6, 6 , 6, 7, 8, 9, 4, 4]
# ans=[]
# temp=[lst[0]]
# for i in range(1,len(lst)):
#     if lst[i-1]==lst[i]:
#         temp.append(lst[i])
#     else:
#         ans.append(temp)
#         temp=[lst[i]]
        
# print(ans)            
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9]]
# # Write a prython program to remove consecutive (following each other continuously) duplicates (elements) from agiven list.
# lst=[0, 0 , 1 ,2, 3, 4, 4, 5, 6, 6 , 6, 7, 8, 9, 4, 4]
# lst1=[0]
# for i in lst:
#     # if i not in lst1:
#     if lst1[-1] != i:    
#         lst1.append(i)
# print(lst1)         
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
# myString = "python Tu'torials"
# print(myString[-3:8:-1])
# print(myString[-2:4:-1])
# airot'
# lairot'uT n
# #split
# str="hello user i, am - learning python"
# lst=str.split(sep="-")
# print(lst)
# ['hello user i, am ', ' learning python']
# word_list = ['hello','user', 'i', 'am', 'learning', 'python']
# temp=" "
# print(temp)
# (' ',)
# x= "hello,everyone.lets,learn,python."
# x=x.replace('.','$')
# x=x.replace(',','.')
# x=x.replace('$',',')
# print(x)
# hello.everyone,lets.learn.python,
