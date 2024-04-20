#define function to display the main menu interface
def main_menu():
    #loop that keeps program running until the user decides to exit the program
    while True:
        #welcome message and the functionalities
        print("\nWelcome to Apache Airlines Seat Booking System!")
        print("\n1. Check seat availability")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        #ask the user to make a choice from the menu options
        choice= input("\nEnter your choice (1-5): ")

        #if statement to connect the users choice to the right function
        if choice == '1':
            check_seat_availability(input("Enter seat id: "))
        elif choice == '2':
            book_seat(input("Enter seat id: "))
        elif choice == '3':
            free_seat(input("Enter seat id: "))
        elif choice == '4':
            show_booking_state()
        elif choice == '5':
            exit_program()
            # Exit the loop to terminate the program
            break
        else:
            print("Invalid choice. Please try again.")

#list all the seats on the jet
bookable_seats = ['1A', '2A', '3A', '4A','1B', '2B', '3B', '4B', '1C', '2C',
                  '3C', '4C', '1D', '2D', '3D', '4D', '1E', '2E', '3E', '4E',
                  '1F', '2F', '3F', '4F', '77A', '78A', '79A', '80A', '77B', '78B', '79B', '80B',
                   '79D', '80D', '79E', '80E', '79F', '80F']
#initially all seats are free
free_seats = list(bookable_seats)
#initially zero seats are booked
booked_seats = []
#define function to check the avaiability of the seats
def check_seat_availability(seat_id):
    #Check if the specified seat is free and available for booking
    if seat_id in free_seats:
        print(f"Seat {seat_id} is available.")
        return True
    else:
        print(f"Seat {seat_id} is not available.")
        return False

#define function to book a seat if available
def book_seat(seat_id):
    if check_seat_availability(seat_id):
        free_seats.remove(seat_id)
        booked_seats.append(seat_id)
        print(f"Seat {seat_id} has been successfully booked.")
    else:
        print(f"Seat {seat_id} cannot be booked.")

#define function to cancel a seat
def free_seat(seat_id):
    if seat_id in booked_seats:
        booked_seats.remove(seat_id)
        free_seats.append(seat_id)
        print(f"Booking for seat {seat_id} has been cancelled.")
    else:
        print(f"Seat {seat_id} is not currently booked.")

#define function to show the current booking state
def show_booking_state():
    pass

#define function to exit the program
def exit_program():
    pass

#start program
if __name__ == "__main__":
    main_menu()