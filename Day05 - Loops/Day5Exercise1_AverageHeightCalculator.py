#Not allow to use count() or len() in for loop

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

height_total = 0
index = 0

for height in student_heights:
  height_total += height
  index += 1


average_height = int(round(height_total / index))
print(f"The average height of the class is {average_height}.")