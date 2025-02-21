#
def get_options_ratio(option, total):
    if total == 0:
        return "Total cannot equal zero"
 
    ratio= option/total
    return ratio

def get_faculty_rating(ratio):
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio >0.8:
        return "Very Good"
    elif ratio >0.7:
        return "Good"
    elif ratio >0.6:
        return "Needs Improvement"
    elif 0 <= ratio < 0.59:
        return "Unacceptable"

