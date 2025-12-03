
investment_amount = float(input("Enter amount invested: "))
number_of_years = float(input("Enter number of years: "))
interest_rate = float(input("Enter interest rate: "))



print("Years\tPercent\t ROI")
for year in range(1,30):

    investment_amount += (investment_amount * (interest_rate / 100))
    print(f'{number_of_years},     {interest_rate},     {investment_amount}')
