# Display a welcome message
print("Welcome to Imo Bank")

# Assign a PIN
PIN = 1234

# Assign an account balance
account_balance = 1000000

# Assign a minimum account balance
minimum_balance = 1000

# Ask the user for the PIN
input_PIN = int(input("Please enter your PIN: "))

# Process operations
while (input_PIN == PIN):
    # Display a menu
    menu = int(input("\n1. Withdrawal" +
                     "\n2. Deposit" +
                     "\n3. Check Balance" +
                     "\n4. Transfer" +
                     "\nPlease select an operation: "))

    # Withdrawal
    if (menu == 1):
        # Prompt the user for the amount of money they want to withdraw
        withdrawal_amount = int(input("\nPlease enter how much you want to withdraw: "))

        # Ensure that the minimum balance is maintained
        if (account_balance - minimum_balance >= withdrawal_amount):
            account_balance = account_balance - withdrawal_amount
            print("Please take your money")
        else:
            print("Insufficient Funds")
            break

        # Ask the user if they want to continue
        option = int(input("\nDo you want to perform another transaction?" +
                           "\n1. Yes" +
                           "\n2. No" +
                           "\nPlease select an option: "))

        # Process the options
        if (option == 1):
            input_PIN = int(input("\nPlease enter your PIN: "))

            if (input_PIN == PIN):
                continue
            else:
                print("Invalid PIN")
                break
        elif(option == 2):
            print("Thank you for banking with us.")
            break

    # Deposit Money
    elif (menu == 2):
        # Prompt the user for an amount to be deposited
        deposit_amount = int(input("\nPlease enter how much money you want to deposit: "))

        # Check that the amount is greater than 0
        if (deposit_amount > 0):
            print("\nPut in the money.")
            print("\nYour deposit was successful.")
            account_balance = account_balance + deposit_amount
        else:
            print("Invalid amount")

        # Ask the user if they want to continue
        option = int(input("\nDo you want to perform another transaction?" +
                          "\n1. Yes" +
                          "\n2. No" +
                          "\nPlease select an option: "))

        # Process the options
        if (option == 1):
            input_PIN = int(input("\nPlease enter your PIN: "))

            if (input_PIN == PIN):
                continue
            else:
                print("Invalid PIN")
                break
        elif (option == 2):
            print("Thank you for banking with us.")
            break
    
    # Account Balance
    elif (menu == 3):
        print("\nYour account balance is ", account_balance)

        # Ask the user if they want to continue
        option = int(input("\nDo you want to perform another transaction?" +
                          "\n1. Yes" +
                          "\n2. No" +
                          "\nPlease select an option: "))

        # Process the options
        if (option == 1):
            input_PIN = int(input("\nPlease enter your PIN: "))

            if (input_PIN == PIN):
                continue
            else:
                print("Invalid PIN")
                break
        elif (option == 2):
            print("Thank you for banking with us.")
            break

    # Transfer
    elif (menu == 4):
        # Ask the user for how much they want to transfer
        if (menu == 4) :
            transfer_value = int(input("\nHow much do you want to transfer? "))

        # If the value is less than N5000, there is a charge of N50
        if ((transfer_value > 0) and (transfer_value < 5000)) :
            print("\nThere is a service charge of N10.")
            transfer_value = transfer_value + 10
        # If the value is greater than or equal to N5000 or less than or equal to N50000, there is a charge of N25   
        elif (transfer_value >= 5000) and (transfer_value <= 50000) :
            print("\nThere is a service charge of N25.")
            transfer_value = transfer_value + 25
        elif(transfer_value > 50000):
            print("\nThere is a service charge of N50.")
            transfer_value = transfer_value + 50
        else:
            print("Invalid amount!")

        # Ask the user if they want to send the money
        option = int(input("\nDo you want to proceed?" +
                  "\n1. Yes" +
                  "\n2. No" +
                  "\nPlease select an option: "))

        # Process the options
        if (option == 1):
            print("\nYour transfer was successful.")
            account_balance = account_balance - transfer_value
        elif (option  ==2):
            print("\nThank you for banking with us.")
            break

        # Ask the user if they want to continue
        option = int(input("\nDo you want to perform another transaction?" +
                          "\n1. Yes" +
                          "\n2. No" +
                          "\nPlease select an option: "))

        # Process the options
        if (option == 1):
            input_PIN = int(input("\nPlease enter your PIN: "))

            if (input_PIN == PIN):
                continue
            else:
                print("Invalid PIN")
                break
        elif (option == 2):
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid Selection!")
    else:
        print("Invalid Selection!")
        break
else:
    print("Invalid PIN")

# Send off
print("\nHave a great day!")
