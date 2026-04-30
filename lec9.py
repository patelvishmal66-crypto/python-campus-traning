# # ASSIGNMENT = 1

# # Q1. Write a Python program to create two sets, A and B, and find the elementsthat are common to both sets. 

# from enum import unique


# set1={1,2,3,4,5}
# set2={3,4,5,6,7}

# print(set1 & set2)
# print(set1.intersection(set2))

# # Q2. Write a Python program to create two sets, X and Y, and find the elementsthat are unique to each set (not present in both)
# setx={10,20,30,40}
# sety={30,40,50,60}
# print(setx ^ sety)
# print(setx.symmetric_difference(sety))


# # Q3. Write a Python program to check if all elements of one set are contained within another set. 
# set1={1,2,3}
# set2={1,2,3,4,5}  
# print(set1.issubset(set2))


# # Q4. Write a Python program which create a new set from given two sets have  only that elements .
# seta={2,4,6}
# setb={1,3,5}
# setc= seta.symmetric_difference(setb)
# print(setc)


# # Q5. Write a Python program to combine all elements from three different sets into one.
# set1={1,2}
# set2={2,3}
# set3={3,4}
# set4=set1|set2|set3
# print(set4)


# # Q6. Write a Python program to find all elements that are in one set but not in the another set.
# seta={10,20,30}
# setb={20,30,40}
# setc=seta.difference(setb)
# print(setc)


# # Q7. Write a Python program to remove a specific element(n) from a set, butonly if it exists in the set.
# set1={1,2,3,4,5}
# set1.discard(2)
# print(set1)




