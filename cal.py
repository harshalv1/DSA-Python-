def calculate_total_amount(years, monthly_investment, increase_rate, return_rate, inflation_rate):
    total_amount = 0
    total_amount_without_inflation = 0
    monthly_investment *= (1 + increase_rate)  # Initial investment for the first month

    for year in range(1, years + 1):
        yearly_investment = monthly_investment * 12
        total_amount += yearly_investment

        # Calculate compound interest for the current year
        total_amount *= (1 + return_rate)

        # Calculate the investment for the next year with the increased amount
        monthly_investment *= (1 + increase_rate)

        # Calculate the total amount without inflation for comparison
        total_amount_without_inflation += yearly_investment
        total_amount_without_inflation *= (1 + return_rate)

    # Adjust for inflation
    total_amount /= (1 + inflation_rate)

    return total_amount, total_amount_without_inflation


years_investment = 15
monthly_investment = 20000
increase_rate = 0.15
return_rate = 0.14
inflation_rate = 0.08

total_amount_with_inflation, total_amount_without_inflation = calculate_total_amount(
    years_investment, monthly_investment, increase_rate, return_rate, inflation_rate
)

print(f"Total amount after {years_investment} years (without considering inflation): {round(total_amount_without_inflation, 2)}")
print(f"Total amount after {years_investment} years (adjusted for inflation): {round(total_amount_with_inflation, 2)}")
