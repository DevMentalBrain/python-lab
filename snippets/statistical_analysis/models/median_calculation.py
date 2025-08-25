import numpy as np

def median_calculation(array):
    central_value = array.size
    if (central_value % 2) == 0:
        median_element_1 = array[(central_value - 1) // 2]
        median_element_2 = array[((central_value - 1) // 2) + 1]

        return (median_element_1 + median_element_2) / 2
    else: 
        return array[(central_value - 1) // 2]