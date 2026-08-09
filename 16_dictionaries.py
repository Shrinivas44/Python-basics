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

#Dictionary + User Input
marks = {"Math": 80,"Python": 90,"AI": 85,"DBMS": 75,"Java": 60}
subject = input("Enter a Subject : ")
print(marks[subject])

#Search Student Information
students = {"Rahul": 85,"Priya": 92,"Shrinivas": 78,"Arun": 88}
name = input("Enter a Name : ")
if name in students:
  print(students[name])
else:
  print("student not found")

#Dictionary + Function
def get_marks(student, name):
  if name in student:
    return student[name]
  else:
    return "student not found"
students = {"Rahul": 85,"Priya": 92,"Shrinivas": 78,"Arun": 88}
print(get_marks(students, "Priya"))

#Dictionary + Function + Loop
def find_top_students():
  result = []
  students = {"Rahul": 85,"Priya": 92,"Shrinivas": 78,"Arun": 88}
  for keys, values in students.items():
    if values >= 85:
      result.append(keys)
  return result
print(find_top_students())

# Find the Top Student
def find_top_student():
  students = {"Rahul": 85,"Priya": 92,"Shrinivas": 78,"Arun": 88}
  count = 0
  result = "hii"
  for name, mark in students.items():
    if mark >= count:
      count = mark
      result = name
  return result
print(find_top_student())

# Find the Lowest Student
def find_top_student():
  students = {"Rahul": 85,"Priya": 92,"Shrinivas": 78,"Arun": 88}
  count = 0
  lowest_mark = list(students.values())[0]
  result = "hii"
  for name, mark in students.items():
    if lowest_mark >= mark:
      result = name
      lowest_mark = mark
  return result   
print(find_top_student())

# Dictionary + Nested Data
student = {"name": "Shrinivas","skills": ["Python", "SQL", "Machine Learning"]}
print(student["name"])
print(student["skills"])
print(student["skills"][0])



























      
  
  
  



































