import time
pin1 =1213
Balance=50000
print("Welcome To Your SBI ATM")
print("Insert Your Card: ")
print("1. Yes")
print("2. No")
card=int(input())
if card==1:
    print("Select Prefered Language")
    print("1. English")
    print("2. Kannada")
    print("3. Hindi")
    lang=int(input())
    if lang==1:
        print("Enter Your Pin: ")
        pin=int(input())
        if pin==pin1:
            print("Select Your Account type")
            print("1. Current Account")
            print("2. Savings Account")
            print("3. cancel Transaction")
            acc=int(input())
            if acc==1:
                print("enter the withdrawl amount: ")
                amt=int(input())
                if amt<=Balance:
                    print("transaction processed")
                    time.sleep(2)
                    print("Collect your cash")
                    time.sleep(2)
                    Balance -= amt
                    print("Remaining Balance in you accountis: ",Balance)
                elif amt>=Balance:
                    print("your Bank Balance is Low")
                    time.sleep(1)
                    print("check your bank balance")
                else:
                    print("Transaction declined")
            elif acc==2:
                print("enter the withdrawl amount")
                if amt <= Balance:
                    print("transaction processed")
                    time.sleep(2)
                    print("Collect your cash")
                    time.sleep(1)
                    Balance -= amt
                    print("Remaining Balance in you accountis: ",Balance)
                elif amt>=Balance:
                    print("your Bank Balance is Low")
                    time.sleep(1)
                    print("check your bank balance")
                else:
                    print("Transaction declined")
            else:
                print("transaction cancelled")
                print("remove your card")
        else:
            print("Error,Transaction Declined")
    else:
        print("Please Select Language English")
else:
    print("Insert Your Card Properly")