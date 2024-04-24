def calculate_electricity_bill(units_consumed, rate_per_unit):
    return units_consumed * rate_per_unit

units_consumed = float(input("Enter the units consumed: "))
rate_per_unit = float(input("Enter the rate per unit: "))

bill_amount = calculate_electricity_bill(units_consumed, rate_per_unit)
print("Electricity bill amount:", bill_amount)
