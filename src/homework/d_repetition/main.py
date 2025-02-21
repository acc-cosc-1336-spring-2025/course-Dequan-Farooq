import repetition 

def display_menu():
    print("1- Factorial")
    print("2- Sum of odd numbers")
    print("3- Exit")

def get_valid_number(min_value, max_value):

    while True:
        num = input(f'Enter a number between {min_value} and {max_value}: ')
        try:
            num = int(num)
            if min_value < num < max_value:  
                return num
            else:
                print(f"Please enter a number greater than {min_value} and less than {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def ask_to_continue():
    """Asks the user if they want to continue or exit."""
    while True:
        choice = input('Do you want to continue? (yes/no): ').strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print('Invalid input. Please enter "yes" or "no".')

def run_menu():
    user_option = '0'  

    while user_option != '3':
        display_menu()  

        user_option = input('Homework 3 Menu (1, 2, or 3): ')

        if user_option == '1':
            
            num = get_valid_number(0, 10)
            result = repetition.get_factorial(num)
            print(f"Factorial of {num} is: {result}")
        
        elif user_option == '2':
            
            num = get_valid_number(0, 100)  
            result = repetition.sum_odd_numbers(num)
            print(f"Sum of odd numbers up to {num} is: {result}")
        
        elif user_option == '3':
            print("Exiting the program...")
        
        else:
            print('Invalid entry. Please choose 1, 2, or 3.')

        
        if user_option != '3' and not ask_to_continue():
            print("Exiting the program...")
            break 


if __name__ == "__main__":
    run_menu()






