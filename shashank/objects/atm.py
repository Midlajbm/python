# Bal = 10000 
# cpin = '8990'
# import time

# def cash_withdrawal():
#     global Bal
#     print("Enter the amount you want to withdraw:")
#     withdrawal_amount = int(input())
#     if withdrawal_amount <= Bal:
#         print("Wait for a moment, your cash is being processed")
#         print("Collect your cash")
#         Bal -= withdrawal_amount
#         print(f"Remaining balance: ₹{Bal}")
#     else:
#         print("Balance is insufficient. Please check your balance.")
#         print("Transaction Declined")

# def account_type():
#                 print("Select Your Account Type:")
#                 print("1. Current Account")
#                 print("2. Savings Account")
#                 acc_type = int(input("Enter your account type: "))
#                 if acc_type == 1:
#                     print("Current Account selected.")
#                     cash_withdrawal()
#                 elif acc_type == 2:
#                     print("Savings Account selected.")
#                     cash_withdrawal()
#                 else:
#                      print("Invalid Account Type")
#                      print("Transaction Declined")
# print("Welcome To SBI ATM")
# def lang():
#     print("Choose your language:")
#     print("1. English")
#     print("2. Hindi")
#     print("3. Kannada")

#     lang = int(input("Enter your choice: "))
    
#     if lang == 1:
#         pin = input("Enter your PIN: ")
#     elif lang == 2:
#         pin = input("अपना पिन दर्ज करें: ")
#     elif lang == 3:
#         pin = input("ನಿಮ್ಮ ಪಿನ್ ನಮೂದಿಸಿ : ")
#     else:
#         print("Invalid language selection")
#         print("Transaction Declined")
#         return

#     if pin == cpin:
#         print("Welcome to your account")
#     else:
#         print("Incorrect PIN")
#         print("Transaction Declined")
#         return

#     print("1. Balance Enquiry")
#     print("2. Cash Withdrawal")
#     print("3. Exit")
    
#     choice = int(input("Enter your choice: "))
    
#     if choice == 1:
#         print(f"Your Bank Balance is: ₹{Bal}")
#     elif choice == 2:
#         account_type()
#     elif choice == 3:
#         print("Transaction Cancelled")
#     else:
#         print("Invalid option")
#         print("Transaction Cancelled")

#     print("Thank you for Visiting Union Bank ATM.")
#     print("Please remove your card.")

# lang()
import tkinter as tk
from tkinter import messagebox
import time

# Initial Data
pin1 = 1213
balance = 50000
lang = "English"

# Main App Window
root = tk.Tk()
root.title("SBI ATM")
root.geometry("400x400")
root.resizable(False, False)

def reset():
    for widget in root.winfo_children():
        widget.destroy()

def insert_card_screen():
    reset()
    tk.Label(root, text="Welcome to Your SBI ATM", font=("Helvetica", 16)).pack(pady=20)
    tk.Label(root, text="Insert Your Card:").pack(pady=10)
    tk.Button(root, text="Insert", command=language_selection).pack()
    tk.Button(root, text="Cancel", command=root.quit).pack(pady=5)

def language_selection():
    reset()
    tk.Label(root, text="Select Preferred Language", font=("Helvetica", 14)).pack(pady=20)
    tk.Button(root, text="English", command=enter_pin).pack(pady=5)
    tk.Button(root, text="Kannada", command=lambda: unsupported_language("Kannada")).pack(pady=5)
    tk.Button(root, text="Hindi", command=lambda: unsupported_language("Hindi")).pack(pady=5)

def unsupported_language(language):
    messagebox.showinfo("Notice", f"{language} not supported yet.\nDefaulting to English.")
    enter_pin()

def enter_pin():
    reset()
    tk.Label(root, text="Enter Your PIN", font=("Helvetica", 14)).pack(pady=20)
    pin_entry = tk.Entry(root, show='*')
    pin_entry.pack()

    def verify_pin():
        if pin_entry.get().isdigit() and int(pin_entry.get()) == pin1:
            account_type_selection()
        else:
            messagebox.showerror("Error", "Incorrect PIN! Transaction Declined")
            insert_card_screen()

    tk.Button(root, text="Submit", command=verify_pin).pack(pady=10)

def account_type_selection():
    reset()
    tk.Label(root, text="Select Account Type", font=("Helvetica", 14)).pack(pady=20)
    tk.Button(root, text="Current Account", command=lambda: withdraw_amount("Current")).pack(pady=5)
    tk.Button(root, text="Savings Account", command=lambda: withdraw_amount("Savings")).pack(pady=5)
    tk.Button(root, text="Cancel Transaction", command=cancel_transaction).pack(pady=10)

def withdraw_amount(account_type):
    reset()
    tk.Label(root, text=f"{account_type} Account Selected", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(root, text="Enter Withdrawal Amount").pack()
    amt_entry = tk.Entry(root)
    amt_entry.pack()

    def process_withdrawal():
        global balance
        if not amt_entry.get().isdigit():
            messagebox.showwarning("Invalid", "Please enter a valid amount.")
            return

        amt = int(amt_entry.get())
        if amt <= balance:
            time.sleep(1)
            balance_label = f"Transaction Successful.\nPlease Collect Your Cash.\nRemaining Balance: ₹{balance - amt}"
            balance -= amt
            messagebox.showinfo("Success", balance_label)
            insert_card_screen()
        else:
            messagebox.showerror("Error", "Insufficient Balance")
            insert_card_screen()

    tk.Button(root, text="Withdraw", command=process_withdrawal).pack(pady=10)

def cancel_transaction():
    messagebox.showinfo("Cancelled", "Transaction Cancelled\nPlease remove your card.")
    insert_card_screen()

# Start with Card Insertion Screen
insert_card_screen()
root.mainloop()
