
# Constants
EMPTY_WEIGHT = 1471    # lbs
GRAVITY_CENTER = 85.9  # in
FRONT_SEATS_MA = 85.5  # in
FUEL_TANKS_MA = 95     # in
REAR_SEATS_MA = 181.1  # in
MAX_RAMP_WEIGHT = 2400 # lbs
MAX_FUEL = 50          # US Gallons

# Program welcome message and data
title = "\nWelcome to the '1965 Piper Cherokee PA-28-180' Flight Approval System\n"
table_title = "\nAircraft specifics\n" + ((len("Empty Weight           : 1,471 lbs") + 8) * '-')

data_table = (
    "\n\tEmpty Weight           : 1,471 lbs\n"
    "\tCenter of Gravity      : 85.9 in\n"
    "\tFront Seats Moment Arm : 85.5 in\n"
    "\tFuel Tank Moment Arm   : 95 in\n"
    "\tRear Seats Moment Arm  : 181.1 in\n"
    "\tMaximum Ramp Weight    : 2400 in\n"
    "\tMaximum Fuel           : 50 lbs\n"
)

print(title, table_title, data_table, ((len("Empty Weight           : 1,471 lbs") + 8) * '-'))

def collecting_information():
    # Collecting information
    while True:
        fuel_amount = float(input("How much fuel is on board (in US Gallons)? "))
        if ((fuel_amount >= 0) and (fuel_amount <= 50)):
            break
        else:
            print("\nPlease enter a weight that is between 0-50 lbs please.\n")
            continue

    pilot_weight =  float(input("What is the weight of the pilot (in lbs)? "))
    copilot_weight = float(input("What is the weight of the co-pilot (in lbs)? "))
    passenger_weight_1 = float(input("What is the weight of passenger one? (if no passenger enter 0) "))
    passenger_weight_2 = float(input("What is the weight of passenger two? (if no passenger enter 0) "))
    
    total_pilot_weight = pilot_weight + copilot_weight
    total_passenger_weight = passenger_weight_1 + passenger_weight_2

    # Fuel weight
    hundred_low_lead = 6
    total_fuel_weight = fuel_amount * hundred_low_lead

    # Calculating ramp weight
    ramp_weight = (
        total_fuel_weight + pilot_weight + copilot_weight + 
        passenger_weight_1 + passenger_weight_2 + EMPTY_WEIGHT
    )

    if (ramp_weight > MAX_RAMP_WEIGHT):
        print(f"Ramp weight is over the limit by {MAX_RAMP_WEIGHT - ramp_weight} lbs")

    return total_pilot_weight, total_passenger_weight, total_fuel_weight, ramp_weight

def current_flight_data(ramp_weight, actual_gravity_center):
    print("\nCurrent flight data")
    print('-' * 46)
    print(f"\tCurrent Weight  : {ramp_weight} [lbs]")
    print(f"\tMaximum Weight  : {MAX_RAMP_WEIGHT} [lbs]")
    print(f"\n\tCurrent Balance : {round(actual_gravity_center, 4)} [in]")
    print("\tBalance Range   : 86.7 < x < 95.8 [in]")
    print('-' * 46)
                                            
def moment_calculations():
    print("")
    pilots, passengers, fuel_weight, ramp_weight = collecting_information()
    moment = (FRONT_SEATS_MA * pilots) + (REAR_SEATS_MA * passengers) + (FUEL_TANKS_MA * fuel_weight) + (EMPTY_WEIGHT * GRAVITY_CENTER)
    actual_gravity_center = moment / ramp_weight
    
    if ((actual_gravity_center >= 86.7) and (actual_gravity_center <= 95.8)):
        print("\nThe aircraft is within the weight and balace. This plane is safe to be flown. ")
        current_flight_data(ramp_weight, actual_gravity_center)
    else:
        print("\nThe aircraft is NOT within the weight and balance. Due to this, this plane should NOT be flown. ")
        current_flight_data(ramp_weight, actual_gravity_center)

while True:
    moment_calculations()

    print("\nProgram Commands")
    print(str((len("Program Commands") + 2) * '-'))
    print("\tRUN  : '0'\n")
    print("\tEXIT : '1'\n")
    print(str((len("Program Commands") + 2) * '-'))

    user_command = int(input("\nRun or exit the program? "))
    if (user_command == 1):
        print("\nThank you for using the '1965 Piper Cherokee PA-28-180' Flight Approval System")
        break
    
