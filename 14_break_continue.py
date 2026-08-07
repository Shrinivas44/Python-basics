# Example 1: Break Statement
i = 1
while True:
  print(i)
  if i == 6:
    break
  i += 1

# Example 2: Continue Statement
for i in range(1,11):
  if i == 5:
    continue
  print(i)

# Example 3: Skip Even Numbers
for i in range(1,11):
  if i%2 == 0:
    continue
  print(i)

# Example 4: Password Checker
password = "python123"
while password:
  i = input("Enter a Password : ")
  if password == i:
     print("Access Granted")
     break

# Example 5: Number Guessing Game
secret_number = 7
while secret_number:
  user_guess_number = int(input("Enter a Number : "))
  if secret_number == user_guess_number:
     print("Correct Guess!")
     break
  else:
     print("Try Again")

# Example 6: Input Validation
while True:
  number = int(input("Enter a Number : "))
  if number <= 0:
    print("Invalid Input")
  else:
    print("Valid Number")
    break
  







    


    
     
              
