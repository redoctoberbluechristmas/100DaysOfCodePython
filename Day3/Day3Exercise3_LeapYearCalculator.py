#Every year divisible by 4 is a leap year.
#Unless it is divisible by 100, and not divisible by 400.


#Conditional with multiple branches

year = int(input("Which year do you want to check? "))

if(year % 4 == 0):
  if(year % 100 == 0):
    if(year % 400 == 0):
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
      print("Leap year.")
else:
  print("Not leap year.")

#Refactored using more condense conditional statement.

#"If a year is divisible by 4, and it is either not divisible by 100, or is not not divisible by 100 but is 
# divisible by 400, then it is a leap year. Otherwise, it is not a leap year."
if(year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
  print("Leap year.")
else:
  print("Not leap year.")