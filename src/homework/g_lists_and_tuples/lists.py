#
def get_lowest_list_value(lst):
    
    lowest_value = float ('inf')

    for value in lst:
        if value < lowest_value:
            lowest_value = value
            
    return lowest_value



def get_highest_list_value(lst):
    
    highest_value = float ('-inf')

    for value in lst:
        if value > highest_value:
            highest_value = value
            
    return highest_value
