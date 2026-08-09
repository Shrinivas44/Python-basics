# Create a tuple named fruits containing, and print the first element
fruits = ("Apple","Banana","Orange","Mango")
print(fruits)
print(fruits[0])

# Tuple Length
numbers = (10, 20, 30, 40, 50)
print(len(numbers))

# Tuple Loop
colors = ("Red", "Blue", "Green", "Yellow")
for color in colors:
  print(color)

# Tuple count()
numbers = (5, 10, 5, 20, 5, 30)
print(numbers.count(5))

# Tuple index()
numbers = (10, 20, 30, 40, 50)
print(numbers.index(40))

# Sets
numbers = {5, 5, 10, 10, 15, 20, 20}
print(numbers)

# Add to a Set
colors = {"Red", "Blue", "Green"}
colors.add("Yellow")
print(colors)

# Remove from a Set
colors = {"Red", "Blue", "Green", "Yellow"}
colors.remove("Blue")
print(colors)

# Check if an Item Exists in a Set
languages = {"Python", "Java", "C++", "JavaScript"}
if "Python" in languages:
  print("python found")
else:
  print("Not found")

# Set union()
python = {"Rahul", "Priya", "Arun"}
java = {"Priya", "Kiran", "Arun"}
all_student = python.union(java)
print(all_student)

# Set intersection()
python = {"Rahul", "Priya", "Arun", "Kiran"}
java = {"Priya", "Kiran", "Vijay"}
common = python.intersection(java)
print(common)

# Set Difference
python = {"Rahul", "Priya", "Arun", "Kiran"}
java = {"Priya", "Kiran", "Vijay"}
only_student = python.difference(java)
print(only_student)

# symmetric_difference()
python = {"Rahul", "Priya", "Arun"}
java = {"Priya", "Kiran", "Arun"}
result = python.symmetric_difference(java)
print(result)

# Remove All Items from a Set
numbers = {10, 20, 30, 40}
numbers.clear()
print(numbers)





































