#driving license eligibility
age = int(input("Enter your age : "))
if age >= 18:
  ll = input("Do you have a learner license? (yes/no) : ")
  if ll == "yes":
    print("Eligible for Driving Test")
  else:
    print("Get Learner License First")
else:
  print("Not Eligible by Age")
