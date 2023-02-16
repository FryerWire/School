
function [] = WBcalculator()    
    % Constants
    EMPTY_WEIGHT = 1471;    % lbs
    GRAVITY_CENTER = 85.9;  % in
    FRONT_SEATS_MA = 85.5;  % in
    FUEL_TANKS_MA = 95;     % in
    REAR_SEATS_MA = 181.1;  % in
    MAX_RAMP_WEIGHT = 2400; % lbs
    MAX_FUEL = 50;          % US Gallons

    % Program welcome message and data
    dashes = "---------------------------------------------------------------------";

    title = "\nWelcome to the '1965 Piper Cherokee PA-28-180' Flight Approval System\n";
    table_title = "\nDry static flight data\n" + dashes;

    data_table = ( ...
        "\n\tEmpty Weight           : 1,471 [lbs]\n" + ...
        "\tCenter of Gravity      : 85.9 [in]\n" + ...
        "\tFront Seats Moment Arm : 85.5 [in]\n" + ...
        "\tFuel Tank Moment Arm   : 95 [in]\n" + ...
        "\tRear Seats Moment Arm  : 181.1 [in]\n" + ...
        "\tMaximum Ramp Weight    : 2400 [in]\n" + ...
        "\tMaximum Fuel           : 50 [US Gallons]\n" ...
    );

    fprintf(title)
    fprintf(table_title)
    fprintf(data_table)
    disp(dashes)

    % Collecting information
    while true
        fuel_amount = input("\nHow much fuel is on board (in US Gallons)? : ");
        if ((fuel_amount >= 0) && (fuel_amount <= MAX_FUEL))
            break
        else
            fprintf("\nERROR: Please enter a weight that is between 0-50 lbs please.\n")
            continue
        end
    end

    pilot_weight =  input("What is the weight of the pilot (in lbs)? : ");
    copilot_weight = input("What is the weight of the co-pilot (in lbs)? : ");
    passenger_weight_1 = input("What is the weight of passenger one? (if no passenger enter 0) : ");
    passenger_weight_2 = input("What is the weight of passenger two? (if no passenger enter 0) : ");
    
    total_pilot_weight = pilot_weight + copilot_weight;
    total_passenger_weight = passenger_weight_1 + passenger_weight_2;

    % Fuel weight
    hundred_low_lead = 6;
    total_fuel_weight = fuel_amount * hundred_low_lead;

    % Calculating ramp weight
    ramp_weight = ( ...
        total_fuel_weight + total_pilot_weight + ...
        total_passenger_weight + EMPTY_WEIGHT ...
    );

    if (ramp_weight > MAX_RAMP_WEIGHT)
        fprintf("Ramp weight is over the limit by %f lbs", -(MAX_RAMP_WEIGHT - ramp_weight))
    end

    front_seat_moment = FRONT_SEATS_MA * total_pilot_weight;
    rear_seat_moment = REAR_SEATS_MA * total_passenger_weight;
    fuel_moment = FUEL_TANKS_MA * total_fuel_weight;
    empty_aircraft_moment = EMPTY_WEIGHT * GRAVITY_CENTER;
    total_moment = front_seat_moment + rear_seat_moment + fuel_moment + empty_aircraft_moment;
    loaded_moment_arm = total_moment / ramp_weight;

    if ((loaded_moment_arm >= 86.7) && (loaded_moment_arm <= 95.8))
        fprintf("\nThe aircraft is within the weight and balace. This plane is safe to be flown. ")
    else
        fprintf("\n\nThe aircraft is NOT within the weight and balance. Due to this, this plane should NOT be flown. ")
    end

    fprintf("\n\nCurrent static flight data\n")
    fprintf(dashes)
    fprintf("\t\nTotal Fuel Weight     : %f [lbs]", total_fuel_weight)
    fprintf("\t\nTotal Ramp Weight     : %f [lbs]", ramp_weight)
    fprintf("\t\nFront Seats Moment    : %f [lbs-in]", front_seat_moment)
    fprintf("\t\nRear Seats Moment     : %f [lbs-in]", rear_seat_moment)
    fprintf("\t\nFuel Moment           : %f [lbs-in]", fuel_moment)
    fprintf("\t\nEmpty Aircraft Moment : %f [lbs-in]", empty_aircraft_moment)
    fprintf("\t\nTotal Moment          : %f [lbs-in]", total_moment)
    fprintf("\t\nLoaded Moment Arm     : %f [in]\n", loaded_moment_arm)
    fprintf(dashes)

end


































