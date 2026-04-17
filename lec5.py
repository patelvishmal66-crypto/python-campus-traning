lst = eval(input("enter"))
print(lst)
4
lst=eval(input("enter list"))
print(lst)
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]+=5
    else:
        lst[i]-=5
print(lst)            
[1, 2, 3, 4, 5, 6, 7, 8]
[-4, 7, -2, 9, 0, 11, 2, 13]
lst=[3,5,7,8,12,10,2,5,8]
print(lst[ : : 5])
print(lst[ -3: : -2])
print(lst[-3:-8: -4])
print(lst[ : : -1])
print(lst[4:10: 3])
print(lst[10:4: 3])
#create empty list
lst=[]
lst1=list()
print (lst)
print(lst1)
lst=[1,2,3,"hello",5.7]
for i in range(len(lst)):
    print(lst[i],end=" ")
print(lst[3][2]) 
#lst=eval(input("enter lista"))
#print(lst)
#max=0
#for i in range(len(lst)):
 #   if lst[i]>lst[i+1]:
  #      max=lst[i]
#print(max)
lst=[7,-4,-2,9,0,11,17,8,19,10]
print(lst[:-5:10])
print(lst[:-5:-10])
[7]
[10]
#add element
lst=[7,-4,-2,9,0,11,17,8,19,10]
#lst.append("hello")
lst.insert(-4,1888)
lst1=[23,43,54]
#lst.extend(lst1)
lst+=lst1
print(lst)
[7, -4, -2, 9, 0, 11, 1888, 17, 8, 19, 10, 23, 43, 54]
lst=[5,3,2,14,8]
r=sum(lst)
ans=[]
for i in lst:
    ans.append(r-i)
print(lst)    
print(ans)    
    
[5, 3, 2, 14, 8]
[27, 29, 30, 18, 24]
lst=[[1,3,5,6,],[3,4,5],[3,5,7],[10,20,30]]
#ans = [15,12,15,6]

ans=[]
for i in range(len(lst)):
    temp=0
    for j in lst[i]:
        temp+=j
    ans.append(temp) 
print(ans)       
[15, 12, 15, 60]
lst=[[1,3,5,6],[3,4,5],[3,5,7],[10,20,30]] 
ans=[]
for i in range(len(lst)):
    temp=lst[i].copy()
    if i%2==0:
        for j in range(len(temp)):
            if temp[j]%2==0:
                temp[j]-=1
        ans.append(temp)    
    else:
        for j in range(len(temp)):
            if temp[j]%2!=0:
                temp[j]+=1
        ans.append(temp)    
print(lst)
print(ans)
[[1, 3, 5, 6], [3, 4, 5], [3, 5, 7], [10, 20, 30]]
[[1, 3, 5, 5], [4, 4, 6], [3, 5, 7], [10, 20, 30]]