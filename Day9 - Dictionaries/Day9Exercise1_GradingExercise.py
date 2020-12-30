student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for name in student_scores:
    if student_scores[name] > 90:
        grade_value = "Outstanding"
    elif student_scores[name] > 80:
        grade_value = "Exceeds Expectations"
    elif student_scores[name] > 70:
        grade_value = "Acceptable"
    else:
        grade_value = "Fail"
    student_grades[name] = grade_value

print(student_grades)