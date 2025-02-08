import decisions

options=int(input('Please enter the amount of options'))

total=int(input('Please enter the total value'))

result=decisions.get_options_ratio(options,total)

print('get_faculty_rating:', result)

faculty_rating = decisions.get_faculty_rating(result)
print("Faculty Rating:", faculty_rating)