# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
# # What the line of code above does is that It's taking the list of fruits and it's signing a variable name, fruit, to each of them
#     print(fruit + " Pie")

# Average height exercise
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

sum = 0
lenght_student_heights  = 0
student_heights = input("Input a list of student heights ").split()
for n in student_heights:
    lenght_student_heights += int(n)
    sum += int(n)
print(sum)
print(lenght_student_heights)
average = sum / lenght_student_heights
print(round (average, 1))












