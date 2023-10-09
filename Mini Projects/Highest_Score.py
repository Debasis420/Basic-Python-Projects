# Highest score of the student in the class.
# Input a list of student scores.
student_scores = input("Input a list of student scores using spacebar").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score=score
    #dont print here we need output after the for loop ends.
  
print(f"The highest score in the class is: {highest_score}")