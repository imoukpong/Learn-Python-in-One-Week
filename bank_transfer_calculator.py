#Welcome the user
print("Welcome to Imo Bank!")

# Ask the user what he or she wants to do
menu = int(input("What do you want to do?" +
                 "\n1. Withdrawal" +
                 "\n2. Deposit" +
                 "\n3. Check balance" +
                 "\n4. Transfer" +
                 "\nPlease select an option: "))

# Ask the user for how much they want to transfer
if (menu == 4) :
   transfer_value = int(input("How much do you want to transfer? "))

# If the value is less than N5000, there is a charge of N50
if (transfer_value < 5000) :
   print("There is a service charge of N10.")

# If the value is greater than or equal to N5000 or less than or equal to N50000, there is a charge of N25   
elif (transfer_value >= 5000) and (transfer_value <= 50000) :
   print("There is a service charge of N25.")
   
else:
    print("There is a service charge of N50.")
