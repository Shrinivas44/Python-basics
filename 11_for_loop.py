#example 1:
for i in range(5):
  print("python")


#Example 2:
for i in range(5):
  print(i)

#Example 3 :Print numbers from 1 to 5.
for i in range(5):
  print(i+1)

#Example 4 : print number from 10 to 15
for i in range(10,16):
  print(i)

#example 5: Multiplication Table
i = int(input("Enter a Number : "))
for j in range(1,11):
    print(f"{i} X {j} = {i*j}")

#Example 6: Sum of Numbers
'''Write a Python program to calculate the sum of numbers from 1 to 5 using a for loop'''
total = 0
for j in range(1,6):
  total += j
print(total)

#Example 7: Print Characters of a String
'''Write a Python program to print each character of a string using a for loop.'''
word = input("Enter a word : ")
for i in range(len(word)):
  print(word[i])


#Example 8: Print Even Numbers
'''Write a Python program to print all even numbers from 1 to 20 using a for loop.'''
for i in range(0,21,2):
  print(i)

#Example 9: Count Even Numbers
'''Write a Python program to count how many even numbers are present
from 1 to 20 using a for loop.'''
count = 0
for i in range(1,21):
  if i % 2 == 0:
    count += 1
print(f"Total Even Numbers = {count}")




















