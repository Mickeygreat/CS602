"""
Test numpy_financial functions
"""
import numpy_financial as npf

int_rate = 0.08  # annual interest rate
years = 10
loan_amt = 100000
month_number = 1

monthly_pmt = npf.pmt(int_rate/12, years*12, -1* loan_amt)
int_part = npf.ipmt(int_rate/12, month_number, years*12,-1*loan_amt)
prin_part = npf.ppmt(int_rate/12, month_number, years*12,-1*loan_amt)

print()
print(f"The monthly payment on ${loan_amt:0.2f} at {int_rate*100:0.2f}%", end=" ")
print(f"for {years} years is ${monthly_pmt:0,.2f}.")
print(f"In month number {month_number} of the loan,")
print(f"${int_part:0.2f} is interest and ${prin_part:0.2f} is applied toward the principal.")
