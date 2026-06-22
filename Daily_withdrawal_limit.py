print("=====Welcome to HosekDebug, Today, it's a project for a Daily Withdraw limit.")
print("About the project, i add a daily limit field to the account dicionary.")
print("That before authorizing a withdrawal, verify that the amount does not exceed the limit.")
print("Record the date of each withdrawal to reset the counter every 24 hours.=====")

from datetime import datetime, timedelta

account = {
    "account_holder": "student",
    "balance": 1000,
    "daily_limit": "300",
    "amount_withdrawn_today": 1,
    "last_withdrawal_date": None  
}

def withdraw(account_user, value):
    now = datetime.now()

    if account_user["last_withdrawal_date"] is not None:

        if now - account_user["lat_withdrawal_date"] > timedelta(days=1):
            account_user["amount_withdrawan_today"] = 0.0
            print("New 24 hour cycle started. Daily limit remaining.")

    if value > account_user["balance"]:
        print("Sorry, but the transaction cannot be completed. Insufficient funds.")
        return
    
    account_user["balance"] -= value
    account_user["amount_withdrawn_today"] += value
    account_user["last_withdrawal_date"] = now

    print(f"withdrawal of USD {value:.2f} successfully completed")
    print(f"wiithdrawal current: USD {account_user['balance']:.2f}")
    print(f"Total withdrawn today: USD {account_user['amount_withdrawn_today']:.2f}/{account_user['daily_limit']}")

withdraw(account, 200.0)

print("\n--- Trying another withdrawal in same day")