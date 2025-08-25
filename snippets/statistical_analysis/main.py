import numpy as np
from models.average_calculation import average_calculation
from models.median_calculation import median_calculation

#Average calculation test
student_grades = np.array([5, 8, 10])
print("Student avarege: " + str(average_calculation(student_grades)))

#Median calculation test
dataset = np.array([10, 14, 15, 20, 25, 27, 100])
print("Median of dataset: " + str(median_calculation(dataset)))