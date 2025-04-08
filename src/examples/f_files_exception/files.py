
def write_to_file(file_name):
    file= open (file_name, 'w')

    file.write ('John Locke\n')
    file.write ('David Hume\n')
    file.write ('Edmund Burke\n')

    file.close

def read_from_file(file_name):
    file = open(file_name, 'r')

    file_lines= file.read()
    file.close()

    print(file_lines)


def read_from_file_one_line_at_a_time(file_name):
    file = open(file_name,'r')

    line1= file.readline().rstrip('\n')
    line2= file.readline().rstrip('\n')
    line3= file.readline().rstrip('\n')


    print(line1)
    print(line2)
    print(line3)


def read_from_file_data_w_loop(file_name):
    file= open(file_name, 'r')

    line= file.readline().rstrip('\n')
    while (line != ''):
        print(line)
        line = file.readline().rstrip('\n')

    file.close()

def read_from_file_w_for_(file_name):
    file = open(file_name,'r')

    for line in file:
        print (line.rstrip('\n'))

    file.close()


def write_employee_records(file_name):
    file = open(file_name, 'w')

    choice = "1"
    while choice == '1':
        id = input ('Enter ID:')
        name = input ('Enter Name:')
        dept = input ('Enter department:')

        file.write(id+ '\t')
        file.write(name+ '\t')
        file.write(dept+ '\t')
        
        choice = input('Enter 1 to continue:')
    file.close()

def read_employee_records(file_name):
    file = open(file_name, 'r')

    for employee in file:
        record = employee.split('\t') # creates a list


        id= record[0]
        name = record[1]
        dept = record [2].rstrip('\n')
        
        print(id, record, dept)
    file.close()

def write_prog_lang_list_of_lists(file_name):
    file=open(file_name, 'w')

    prog_langs = [['1980','C++', 'Complex']]

    for lang in prog_langs:
        file.write(lang[0]+'\t')# year
        file.write(lang[1]+'\t') # lan
        file.write(lang[2]+'\t') # diff

    file.close()

def read_prog_lang_list_of_lists(file_name):
    file= open (file_name, 'r')
    list_langs= [] 
    for line in file:
        record= line.split('\t')
        year= record[0]
        lang= record[1]
        level= record[2]

        lang_list= [year, lang, level]
        
        list_langs.append(lang_list)
    print(list_langs)

    file.close()