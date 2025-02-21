def get_factorial(num):
    result = 1
    
    for i in range(1, num + 1):
        result *= i
    
    return result

def sum_odd_numbers(num):
    total_sum= 0
    
    current_number= 1
    
    while current_number <= num:
        total_sum += current_number  
        current_number += 2 

    return total_sum   