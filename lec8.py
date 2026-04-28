# reversing a string
x = "Hello everyone lets learn python"
x= x.split()
x = [word[::-1].lower() for word in x]
x = " ".join(x)
print(x)

#  x='',"",'""'
#x="hello
# x+="H1"
# print(l)
#x="hello"
#----------x-----------x--------x--------x-----
# Q1. Write a Python program to reverse the order of words in a given 
# string without reversing the individual words. 
# Input: "Hello World from Python" 
# Output: "Python from World Hello"
# x="hello everyone lets learn python"
# x=x.split()
# print(x)
# x.reverse()
# print(x)
# x=" ".join(x).capitalize()
# print(x)
#"python learn lets everyone hello"

# x="hello everyone lets learn python"
# # olleh enoyreve stel nrael nohtyp 
# x=x.split()
# #x.reverse()
# x=[word[::-1] for word in x]
# x=" ".join(x)
# print(x)

#----------x-----------x--------x--------x-----
# Q2. Write a Python program to remove all occurrences of a given 
# substring from a string. 
# Input: "This is a test string for testing", "test" 
# Output: "This is a string for ing" 

# x="This is a test string for testing"
# y="test"
# x=x.replace(y, "")
# print(x)


# Q3. Write a Python program that takes a string and a character as 
# input and returns a list of indices where the character occurs in the 
# string. 
# Input: "programming", 'm' 
# Output: [6, 7] 
# x="programming"
# y='m'
# result = [i for i, char in enumerate(x) if char == y]
# print(result)

#----------x-----------x--------x--------x-----

# Q3. Write a Python program to find all unique characters in a given 
# string. 
# Input: "programming" 
# # Output: ['p', 'o', ')r', 'g', 'a', 'm', 'i', 'n']
# x="programming"
# unique_chars = list(set(x))
# print(unique_chars)

#----------x-----------x--------x--------x-----

# Q6. Write a Python program to count the number of words in a given 
# string that start with a specific letter which was taken as a input. 
# Input: "This is a test string for testing", 't' 
# Output: 3
x="This is a test string for testing"
letter='t'
words = x.split()
count = sum(1 for word in words if word.startswith(letter))
print(count)

 