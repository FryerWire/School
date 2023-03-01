
clear, clc

while true
    WBcalculator();
    
    fprintf("\n\n")
    user_command = input("Would you like to run the program again? (Enter '1' for yes or '0' for no): ");
    if ~ ((user_command == 1) || (user_command == 0))
        fprintf("ERROR: Please either enter 'Yes' or 'No")
        continue
    elseif (user_command == 0)
        fprintf("\nThank you for using the '1965 Piper Cherokee PA-28-180' Flight Approval System")
        break
    else
        continue
    end
end
