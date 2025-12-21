# total average
#total and average
import student as s
def calculate_total(marks):
    return sum(marks.values())

def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks) if marks else 0