"""Q5. Write a Python program that:
1. Prompts for user input: a. Room type (Standard or Deluxe) b. Number of nights c. Number of people d. Meal charges (if any)
2. Calculates room charges: Uses appropriate conditional statements to determine the correct rates based on room type and occupancy.
3. Calculates additional charges: Includes taxes, breakfast charges (if applicable), and other service charges.
4. Generates a detailed bill: Clearly lists each charge with a descriptive label (e.g., room rate, tax, breakfast, parking).
5. Provides a subtotal of charges before tax.
6. Displays the total amount due, including all taxes and fees. """

#Print the program title
print("Calculate and print the hotel bill")

# Define Constants
STD_RM_RATE1 = 155
STD_RM_RATE2 = 160
STD_RM_RATE3 = 165

DLX_RM_RATE1 = 195
DLX_RM_RATE2 = 210
DLX_RM_RATE3 = 225

TAX = 0.12
BREAKFAST = 15
PACKING = 25
DISCOUNT_5NIGHTS = 0.9

#Get User Inputs
room_type = input("Please choose room type(standard or deluxe): ").lower()
num_nights = int(input("Please enter the number of nights: "))
num_people = int(input("Please enter the number of people: "))
breakfast = (input("Would you like breakfast (y/n): ")).lower()
parking = (input("Do you need parking (y/n): ")).lower()

#Figure the room rate
room_rate = None
if room_type == 'standard':
    if num_people == 1:
        room_rate = STD_RM_RATE1
    elif num_people == 2:
        room_rate = STD_RM_RATE2
    else:
        room_rate = STD_RM_RATE3

elif room_type == 'deluxe':
    if num_people <= 2:
        room_rate = DLX_RM_RATE1
    elif num_people == 3:
        room_rate = DLX_RM_RATE2
    else:
        room_rate = DLX_RM_RATE3
else:
    print("Error: Invalid Room Type")


#Calculate the room charges
if room_rate is not None:
    room_charges = room_rate* num_nights
    if num_nights >= 5:
        room_charges *= DISCOUNT_5NIGHTS

    if breakfast == "y":
        breakfast_charges = num_people * num_nights* BREAKFAST
        room_charges += breakfast_charges

    if parking == "y":
        parking_charges = num_nights * PACKING
        room_charges += parking_charges

    # Calculate taxes
    tax_charges = room_charges * TAX

    # Calculate total charges
    total_charges = room_charges + tax_charges

    # Display the detailed bill
    print("\nHotel Bill Summary:")
    print(f"Room Type: {room_type.capitalize()}")
    print(f"Number of Nights: {num_nights}")
    print(f"Number of People: {num_people}")
    print("\nCharges Breakdown:")
    print(f"Room Rate per Night: ${room_rate}")
    print(f"Room Charges ({num_nights} nights): ${room_charges:.2f}")
    
    if num_nights >= 5:
        print("Discount (Stays longer than 5 nights): 10%")
    
    if breakfast == "y":
        print(f"Breakfast Charges: ${breakfast_charges:.2f}")

    if parking == "y":
        print(f"Parking Charges: ${parking_charges:.2f}")

    print(f"Tax (12%): ${tax_charges:.2f}")
    print(f"\nTotal Amount Due: ${total_charges:.2f}")

else:
    print("Error: Invalid Room Type")

