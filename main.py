#define function to display the main menu interface
def main_menu():
    #loop that keeps program running until the user decides to exit the program
    while True:
        #welcome message and the functionalities options
        print("\nWelcome to Apache Airlines Seat Booking System!")
        print("\n1. Check seat availability")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        #ask the user to make a choice from the menu options
        choice = input("\nEnter your choice (1-5): ")

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
                   '77C','78C', '79C', '80C', '79D', '80D', '79E', '80E', '79F', '80F']
#initially all seats are free
free_seats = list(bookable_seats)
#initially zero seats are booked
booked_seats = []
#define function to check the availability of the seats
def check_seat_availability(seat_id):
    #Check if the specified seat is free and available for booking
    #check if seat in free_seats list
    if seat_id in free_seats:
        print(f"Seat {seat_id} is available.")
        return True
    #check if seat in booked_seats list
    elif seat_id in booked_seats:
        print(f"Seat {seat_id} is not available.")
        return False
    #check if the seat_id is a valid seat identifier
    else:
        print(f"{seat_id} does not correspond to a valid seat identifier.")
        return False

#define function to book a seat if available
def book_seat(seat_id):
    #check if the seat_id is a valid seat identifier
    if seat_id not in bookable_seats:
        print(f"{seat_id} does not correspond to a valid seat identifier.")
        return

    if check_seat_availability(seat_id):
        free_seats.remove(seat_id)
        booked_seats.append(seat_id)
        print(f"Seat {seat_id} has been successfully booked.")
    else:
        print(f"Seat {seat_id} cannot be booked.")
#define function to cancel a seat
def free_seat(seat_id):
    #check if the seat_id is a valid seat identifier
    if seat_id not in bookable_seats:
        print(f"{seat_id} does not correspond to a valid seat identifier.")
        return

    if seat_id in booked_seats:
        #remove the booked seat list
        booked_seats.remove(seat_id)
        #add it back to the free seat list
        free_seats.append(seat_id)
        print(f"Booking for seat {seat_id} has been cancelled.")
    else:
        print(f"Seat {seat_id} is not currently booked.")

#define function to show the current booking state
def show_booking_state():
    #Print the header explaining the seat status symbols
    print("Display of current seat bookings \nseat id showed and seat status provided on its right "
          "\nR=Reserved\nF=Free to book\nX=Isles \nS=Storage\n")
    #define storage for reference these seats are next to the places that cannot be booked and should be marked with 'S'
    storage = {'79D', '79E', '79F'}

    #rows and columns representing the seat layout
    #'X' is included in rows to handle the special case of the aisle
    #display rows 1-4 and 77-80 as bookable seats
    rows = 'ABCXDEF'
    columns = [1, 2, 3, 4] + [77, 78, 79, 80]
    #loop through each seat position based on the layout
    for row in rows:
        for col in columns:
            #create the seat ID again
            seat = f'{col}{row}'
            #if we're at the aisle row (after 'C'), print 'X' for the aisle
            if row == 'X':
                print('   X  ', end='')
            #print 'S' for storage seats, followed by '-F' to denote that they are not bookable
            elif seat in storage:
                print(' S ',' S ',seat,'-F ', end='')
            #if the seat is free, print the seat ID followed by '-F'
            elif seat in free_seats:
                print(seat,'-F ', end='')
            #if the seat is booked, print the seat ID followed by '-R'
            elif seat in booked_seats:
                print(seat, '-R ', end='')
            else:
                #print spaces for non-existent seat spaces (should not occur with current seat mapping)
                print('   ', end='')
        #new line at the end of each row
        print()

#define function to exit the program
def exit_program():
    print("Thank you for using Apache Airlines Seat Booking System. Goodbye!")

#start program
if __name__ == "__main__":
    main_menu()