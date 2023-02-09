
"""
Project 1: Question 1: '1965 Piper Cherokee PA-28-180' Flight Approval System
Maxwell Seery
"""

# Constants
EMPTY_WEIGHT = 1471    # lbs
GRAVITY_CENTER = 85.9  # in
FRONT_SEATS_MA = 85.5  # in
FUEL_TANKS_MA = 95     # in
REAR_SEATS_MA = 181.1  # in
MAX_RAMP_WEIGHT = 2400 # lbs
MAX_FUEL = 50          # US Gallons

# Program welcome message and data
dashes = ((len("Empty Weight           : 1,471 lbs") + 10) * '-')

title = "\nWelcome to the '1965 Piper Cherokee PA-28-180' Flight Approval System\n"
table_title = "\nDry static flight data\n" + dashes

data_table = (
    "\n\tEmpty Weight           : 1,471 [lbs]\n"
    "\tCenter of Gravity      : 85.9 [in]\n"
    "\tFront Seats Moment Arm : 85.5 [in]\n"
    "\tFuel Tank Moment Arm   : 95 [in]\n"
    "\tRear Seats Moment Arm  : 181.1 [in]\n"
    "\tMaximum Ramp Weight    : 2400 [in]\n"
    "\tMaximum Fuel           : 50 [US Gallons]\n"
)

print(title, table_title, data_table, dashes)

def collecting_information():
    """
    User information collecting in which checks user data compared with the flight constants

    Returns
        - total_pilot_weight (float)     : Total pilot weight in [lbs]
        - total_passenger_weight (float) : Total passenger weight in [lbs]
        - total_fuel_weight (float)      : Total fuel weight in [lbs]
        - ramp_weight (float)            : Total ramp weight in [lbs]
    """

    # Collecting information
    while True:
        fuel_amount = float(input("\nHow much fuel is on board (in US Gallons)? : "))
        if ((fuel_amount >= 0) and (fuel_amount <= 50)):
            break
        else:
            print("\nERROR: Please enter a weight that is between 0-50 lbs please.\n")
            continue

    pilot_weight =  float(input("What is the weight of the pilot (in lbs)? : "))
    copilot_weight = float(input("What is the weight of the co-pilot (in lbs)? : "))
    passenger_weight_1 = float(input("What is the weight of passenger one? (if no passenger enter 0) : "))
    passenger_weight_2 = float(input("What is the weight of passenger two? (if no passenger enter 0) : "))
    
    total_pilot_weight = pilot_weight + copilot_weight
    total_passenger_weight = passenger_weight_1 + passenger_weight_2

    # Fuel weight
    hundred_low_lead = 6
    total_fuel_weight = fuel_amount * hundred_low_lead

    # Calculating ramp weight
    ramp_weight = (
        total_fuel_weight + total_pilot_weight + 
        total_passenger_weight + EMPTY_WEIGHT
    )

    if (ramp_weight > MAX_RAMP_WEIGHT):
        print(f"Ramp weight is over the limit by {-(MAX_RAMP_WEIGHT - ramp_weight)} lbs")

    return total_pilot_weight, total_passenger_weight, total_fuel_weight, ramp_weight
                                            
def moment_calculations():
    """
    Calculates all of the moment data and determines whether these conditions flight worthy

    Prints
        - Flight approval/disapproval
        - Static flight data
    """
    
    pilots, passengers, fuel_weight, ramp_weight = collecting_information()
    
    front_seat_moment = FRONT_SEATS_MA * pilots
    rear_seat_moment = REAR_SEATS_MA * passengers
    fuel_moment = FUEL_TANKS_MA * fuel_weight
    empty_aircraft_moment = EMPTY_WEIGHT * GRAVITY_CENTER
    total_moment = front_seat_moment + rear_seat_moment + fuel_moment + empty_aircraft_moment
    loaded_moment_arm = total_moment / ramp_weight
    
    if ((loaded_moment_arm >= 86.7) and (loaded_moment_arm <= 95.8)):
        print("\n\nThe aircraft is within the weight and balace. This plane is safe to be flown. ")
    else:
        print("\nThe aircraft is NOT within the weight and balance. Due to this, this plane should NOT be flown. ")

    print("\nCurrent static flight data")
    print('-' * 50)
    print(f"\tTotal Fuel Weight     : {round(fuel_weight, 5)} [lbs]")
    print(f"\tTotal Ramp Weight     : {round(ramp_weight, 5)} [lbs]")
    print(f"\tFront Seats Moment    : {round(front_seat_moment, 5)} [lbs-in]")
    print(f"\tRear Seats Moment     : {round(rear_seat_moment, 5)} [lbs-in]")
    print(f"\tFuel Moment           : {round(fuel_moment, 5)} [lbs-in]")
    print(f"\tEmpty Aircraft Moment : {round(empty_aircraft_moment, 5)} [lbs-in]")
    print(f"\tTotal Moment          : {round(total_moment, 5)} [lbs-in]")
    print(f"\tLoaded Moment Arm     : {round(loaded_moment_arm, 5)} [in]")
    print('-' * 50)

while True:
    moment_calculations()

    user_command = str(input("\nWould you like to run the program again? (Enter 'Yes' or 'No'): ")).lower()
    if not ((user_command == "yes") or (user_command == "no")):
        print("ERROR: Please either enter 'Yes' or 'No")
        continue
    elif (user_command == "no"):
        print("\nThank you for using the '1965 Piper Cherokee PA-28-180' Flight Approval System")
        break
    
