import os

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

number_of_heights = 0
sum_of_heights = 0
for height in student_heights:
    sum_of_heights += height
    number_of_heights = number_of_heights + (height/height) 

average_height = round(sum_of_heights/number_of_heights)
print(f"Average height of all students is: {average_height}")
os.system('pause')