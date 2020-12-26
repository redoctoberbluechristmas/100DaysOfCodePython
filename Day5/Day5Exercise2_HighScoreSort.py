# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#Using max function
# print(max(student_scores))
#Not using max function
high_score = 0

for score in student_scores:
  if score > high_score:
    high_score = score

print(f"Today's high score is: {high_score}")


#Using max function
# print(max(student_scores))