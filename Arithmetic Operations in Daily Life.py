#Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? 

# function

def sum_three (bread, peanut_butter, jelly):
    return (bread + peanut_butter + jelly)

bread=2.45
peanut_butter=4.77
jelly=3.29
SANDWICH=bread + peanut_butter + jelly

print ( SANDWICH)

#Task 2: Bank Interest you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700

def compound_interest(principal, rate, time, comp_per_year):
    # change annual rate to a decimal
    rate_decimal = rate / 100

    amount = principal_amount * (1 + rate_decimal / comp_per_year) ** (comp_per_year * time)
    interest_earned = amount - principal

    return amount, interest_earned


principal_amount = 10000
annual_interest_rate = 7
time_in_years = 1
compounding_frequency = 1  # per month

final_amount, earned_interest = compound_interest(
    principal_amount, annual_interest_rate, time_in_years, compounding_frequency
)

print(f"Final amount after {time_in_years} years: ${final_amount:.2f}")


