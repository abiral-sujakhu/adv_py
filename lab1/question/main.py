# create object 
# calculate result and display
#create object
#calculate result
#display
# create object, calculate result, display
from student import student
from operation import calculate_total, calculate_average

# Create student object
s1 = student("Abiral", 101, {"math": 90, "english": 85, "science": 88})

# Display student info
s1.display()

# Calculate and display total and average
total = calculate_total(s1.marks)
average = calculate_average(s1.marks)

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average}")