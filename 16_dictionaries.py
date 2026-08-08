# Example 1: Create and Access Dictionary
student = {"name":"Rahul","age":21,"branch":"aiml"}
print(student["name"])
print(student["age"])
print(student["branch"])

# Example 2: Add and Update Dictionary
student = {"name":"Rahul","age": 21}
student["branch"] = "aiml"
student["age"] = 22
print(student)

# Example 3: Remove Dictionary Item
student = {"name": "Rahul","age": 21,"branch": "AIML"}
del student["age"]
print(student)

# Example 4: Check if Key Exists
student = {"name": "Rahul","age": 21,"branch": "AIML"}
if "branch" in student:
  print("branch found")
else: 
  print("branch not found")

# Example 5: Loop Through Dictionary
student = {"name": "Rahul","age": 21,"branch": "AIML"}
for key in student:
  print(key)

# Example 6: Keys and Values
student = {"name": "Rahul","age": 21,"branch": "AIML"}
for key, value in student.items():
  print(f"{key} : {value}")

# Example 7: Dictionary get()
student = {"name": "Rahul","age": 21}
print(student.get("name"))
print(student.get("branch"))

# Example 8: Dictionary keys() and values()
student = {"name": "Rahul","age": 21,"branch": "AIML"} 
print(student.keys())
print(student.values())

# Example 9: Dictionary pop()
student = {"name": "Rahul","age": 21,"branch": "AIML"}
student.pop("branch")
print(student)

# Example 10: Count Dictionary Items
marks = {"Math": 80,"Python": 90,"AI": 85,"DBMS": 75}
print(len(marks))

# Example 11: Dictionary With Condition
marks = {"Math": 80,"Python": 90,"AI": 85,"DBMS": 75}
for subject, mark in marks.items():
  if mark >= 80:
    print(subject)

#Count how many subjects have marks greater than or equal to 80.
marks = {"Math": 80,"Python": 90,"AI": 85,"DBMS": 75,"Java": 60}
count = 0
for subject,mark in marks.items():
  if mark >= 80:
    count += 1
print(count)














