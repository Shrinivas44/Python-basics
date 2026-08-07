# Example 1: Print Numbers Using While Loop
numbers = 1 
while numbers <= 5:
  print(numbers) 
  numbers += 1

# Example 2: Print Even Numbers
num = 2 
while num <= 10:
  print(num)
  num += 2

# Example 3: Multiplication Table
num = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(f"{num} X {i} = {num*i}")
    i += 1

# Example 4: Sum of Numbers
num = 0
i = 0
while i <= 10:
    num = i + num
    i += 1
print(num)

# Example 5: Countdown
numbers = 10
while numbers >= 1:
  print(numbers) 
  numbers -= 1

# Example 6: Factorial of a Number
num = int(input("Enter a number : "))
i = 1
factorial = 1
while num >= i:
    factorial = factorial*i
    i += 1
print(factorial)





















