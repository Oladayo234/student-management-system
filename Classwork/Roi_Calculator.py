#Ask user for the investment amount
#Ask user for the number of years
#Ask user for the interest rate
#Calculate the yearly return on investment for 10 years
#Display each year


investment_amount = float(input("Enter amount invested: "))
number_of_years = float(input("Enter number of years: "))
interest_rate = float(input("Enter interest rate: "))

#return_on_investment = investment_amount * interest_rate) + investment_amount

print("Years\tPercent\t ROI")
for year in range(1,10):
#    return_on_investment = (investment_amount * (1 + interest_rate) ** number_of_years)
     investment_amount += (investment_amount * (interest_rate / 100))
    print(f'{number_of_years},     {interest_rate},     {investment_amount}')
    
