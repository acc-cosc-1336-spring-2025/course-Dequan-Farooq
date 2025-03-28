from lists import get_highest_list_value, get_lowest_list_value

def display_menu():
    print('1- Show the list low/high values')
    print('2- Exit')

def get_user_input():
    """Prompts the user to enter values until they decide to stop."""
    numbers = []
    while True:
        try:
            value = int(input("Enter a list value: "))
            numbers.append(value)
            
            # After at least 3 values, ask if they want to continue entering values
            if len(numbers) >= 3:
                continue_input = input("Do you want to enter another value? (y/n): ").strip().lower()
                if continue_input == 'n':
                    break
        except ValueError:
            print("Invalid input! Please enter an integer value.")
    return numbers

def run_menu():
    while True:
        display_menu()

        try:
            user_option = int(input("Please choose option 1 or 2: "))
        except ValueError:
            print('Invalid choice, Please choose option one or two')
            continue
        
        if user_option == 1:
            # Prompt the user for list values
            numbers = get_user_input()
            
            # Get the lowest and highest values from the numbers list
            lowest = get_lowest_list_value(numbers)
            highest = get_highest_list_value(numbers)
            
            # Display the values to the user
            print(f"Lowest value: {lowest}")
            print(f"Highest value: {highest}")

        elif user_option == 2:
            print('Exiting the program......')
            break  # Exit the loop and the program
        
        else:
            print("Invalid choice, Please choose option 1 or 2")

# Start the menu program
run_menu()



                            
                             




