def greet():
  print("Hello, Welcome to python")
greet()
greet()
greet()

# Example 2: Function with a Parameter
def greet(name):
  print("Hello",name)
greet("Rahul")
greet("Priya")
greet("Shinivasa")

# Example 3: Function with Two Parameters
def add(a, b):
  print(a+b)
add(10, 20)
add(7, 5)
add(50, 50)

# Example 4: Return a Value
def square(a):
  return a*a
number1 = square(5)
number2 = square(10)
number3 = square(7)
print(number1)
print(number2)
print(number3)

# Example 5: Function With Condition
def check_even(a):
  if a % 2 == 0:
    return "even"
  else:
    return "odd"
number1 = check_even(1)
number2 = check_even(2)
number3 = check_even(3)
print(number1)
print(number2)
print(number3)

# Example 6: Function With Loop
def print_numbers(n):
  for i in range(1,n+1):
    print(i)
print_numbers(5)

# Example 7: Function With a List
def print_fruits():
  fruits = ["Apple", "Banana", "Orange", "Mango"]
  for i in range(len(fruits)):
    print(fruits[i])
print_fruits()

# Example 8: Find Largest Number
def find_largest(numbers):
  return max(numbers)
result = find_largest([10, 25, 7, 40, 15])
print(result)

# Example 9: Get Even Numbers
def get_even_numbers(number):
  a = []
  for i in range(len(number)):
    if number[i] % 2 == 0:
      a.append(number[i])
  print(a)
get_even_numbers([1,2,3,4,5,6])

# Example 10: Count Greater Numbers
def count_greater(number,target):
  count = 0
  for i in range(len(number)):
    if number[i] > target:
      count += 1
  return count
print(count_greater([12,13,14,15,16],15))



























    






















