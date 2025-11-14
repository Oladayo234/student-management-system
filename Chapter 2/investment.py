principal = 1000
rate = 0.07
year_one = 10
year_two = 20
year_three = 30

deposit = int(input("Enter an integer  "))

return_on_investment_year_one = 1000 * (1+0.07) ** year_one
return_on_investment_year_two = 1000 * (1+0.07) ** year_two
return_on_investment_year_three = 1000 * (1+0.07) ** year_three

print("Returns for year one", return_on_investment_year_one, "\nReturns for year two", return_on_investment_year_two, "\nReturns for year one", return_on_investment_year_three)




