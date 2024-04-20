#define function to display the main menu interface
def main_menu():
    #loop that keeps program running until the user decides to exit the program
    while True:
        #welcome message and the functionalities
        print("\nWelcome to Apache Airlines Seat Booking System")
        print("1. Check seat availability")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        #ask the user to make a choice from the menu options
        choice= input("Enter your choice (1-5): ")

        #if statement to connect the users choice to the right function
        if choice == '1':
            check_seat_availability()
        elif choice == '2':
            book_seat()
        elif choice == '3':
            free_seat()
        elif choice == '4':
            show_booking_state()
        elif choice == '5':
            exit_program()
            # Exit the loop to terminate the program
            break
        else:
            print("Invalid choice. Please try again.")

#define function to check the avaiability of the seats
def check_seat_availability():
    pass

#define function to book a seat
def book_seat():
    pass

#define function to cancel a seat
def free_seat():
    pass

#define function to show the current booking state
def show_booking_state():
    pass

#define function to exit the program
def exit_program():
    pass

#start program
if __name__ == "__main__":
    main_menu()