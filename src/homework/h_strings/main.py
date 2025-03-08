from strings import get_hamming_distance
from strings import get_dna_complement

def main():
    while True:
        # Display the menu options
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        # Prompt the user for a choice
        choice = input("Please select an option (1, 2, or 3): ")

        if choice == '1':
            # Option 1: Get Hamming Distance
            dna1 = input("Enter the first DNA sequence: ")
            dna2 = input("Enter the second DNA sequence: ")

            # Call the get_hamming_distance function
            try:
                distance = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {distance}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            # Option 2: Get DNA Complement
            dna = input("Enter the DNA sequence: ")

            # Call the get_dna_complement function
            complement = get_dna_complement(dna)
            print(f"DNA Complement: {complement}")

        elif choice == '3':
            # Option 3: Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()