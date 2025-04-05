from dictionary import get_p_distance_matrix

def display_matrix(matrix):
    """Display the matrix in a readable format with two decimal places."""
    for row in matrix:
        print(' '.join(f'{value:.2f}' for value in row))

def main():
    while True:
       
        print("\nMenu:")
        print("1 - Get p distance matrix")
        print("2 - Exit")

        
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
           
            list_of_lists = []
            print("Enter lists (one list at a time, separated by spaces). Type 'done' when finished:")
            while True:
                user_input = input("Enter list: ")
                if user_input.lower() == 'done':
                    break
                try:
                    
                    list_of_lists.append(user_input.strip().split())
                except Exception as e:
                    print(f"Error parsing input: {e}")
                    continue

           
            try:
                p_distance_matrix = get_p_distance_matrix(list_of_lists)
                print("P-distance matrix:")
                display_matrix(p_distance_matrix)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == "2":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()



