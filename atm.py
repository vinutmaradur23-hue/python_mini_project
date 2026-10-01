# define the class for ATM Machine Simulation
class ATM:
    
    # define the self function of ATM
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []
    
    # This authenticate() function is used to ask user for pin 
    def authenticate(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Try again.")
            return False
    
    # This check_balance() function is used to check the user's current balance
    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")
        self.transaction_history.append("Balance Inquiry")
    
    # This deposit_cash() function is used to deposit the cash by user
    def deposit_cash(self):
        amount = float(input("Enter the amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
            self.transaction_history.append(f"Deposited ₹{amount}")
        else:
            print("Invalid amount.")
    
    # This withdraw_cash() function is used withdraw cash by user
    def withdraw_cash(self):
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount > 0:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
            self.transaction_history.append(f"Withdrew ₹{amount}")
        else:
            print("Invalid amount.")
    
    # This chane_pin() function is used to change the user's pin
    def change_pin(self):
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully!")
                self.transaction_history.append("PIN Changed")
            else:
                print("PINs do not match. Try again.")
        else:
            print("Incorrect PIN.")
    
    # This show_transcation_history() function is used to show the transcation history of user
    def show_transaction_history(self):
        if self.transaction_history:
            print("\nTransaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction}")
        else:
            print("No transactions yet.")

# This atm_menu() function used to call various operations avaiable for ATM Machine Simulation
def atm_menu(atm):
    while True:
        print("\n--- ATM Machine ---")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit_cash()
        elif choice == "3":
            atm.withdraw_cash()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize ATM with a default PIN and balance
atm = ATM(pin="1234", balance=5000)

if atm.authenticate():
    atm_menu(atm)
else:
    print("Authentication failed. Exiting.")
