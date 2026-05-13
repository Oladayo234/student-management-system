
def validate_email(user_input):
    if(len(user_input) >= 8 and "@" in user_input and user_input[0] != "@" and user_input[-1] != "@" ):
        return True
    else:
        return False

print(validate_email("oladayo@gmail.com"))
print(validate_email("@ladayo@gmail.com"))
print(validate_email("oladayo@gmail.co@"))


def calculate_balance(transactions):
    balance = 0
    deposit = 0
    withdraw = 0
    for count in range(len(transactions)):
        if(transactions[count] > 0 ):
            deposit += transactions[count]
        elif(transactions[count] < 0):
            withdraw -= transactions[count]

        balance = deposit - withdraw

    return balance

print(calculate_balance([2,4,6, -1, -2, -3]))


def is_strong_password(password):
    if(len(password)  >= 8):
        return "It is a strong password"
    else:
       return "It is not a strong password"

print(is_strong_password("abcdefgh"))


def calculate_interest(balance, rate, years):
    if(rate < 0):
        raise ValueError("rate can not be less than zero")
    if(years < 1):
        raise ValueError("year can not be less than one")
    
    interest = balance *(1 + rate) ** years
    return interest + balance

print(calculate_interest(1000, 0.05, 2))


def get_transaction_summary(transaction):
    transaction_summary = {"credit": 0, "debit": 0, "net_balance": 0, "transaction_count": 0}
    for count in range(len(transaction)):
        if(transaction[count][0] == "credit"):
            transaction_summary["credit"] += transaction[count][1]
        elif(transaction[count][0] == "debit"):
            transaction_summary["debit"] += transaction[count][1]

        transaction_summary["transaction_count"] += 1
    return transaction_summary
    
print(get_transaction_summary([["credit", 2000], ["debit", 500], ["credit", 300],]))


    
    
    
