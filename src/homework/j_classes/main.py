from class_a import die
def main():
    my_die = die()
    print("Welcome to the Die Roller!")

    while True:
        input("Press Enter to roll the die...")  # Pause until user hits Enter
        my_die.roll()
        print(my_die)  # Calls __str__

        choice = input("Do you want to roll again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thanks for playing!")
            break


# Entry point
if __name__ == "__main__":
    main()
