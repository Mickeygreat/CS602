"""First Group Assignment:

Given the weight of a package calculate the delivery cost according to the following rules:

· A flat fee of $2.00 is applied

· The cost by weight is $6.00 for transporting each 25lbs of the package,

· 3.5% delivery tax is added to the charges.

Sample interaction illustrates input and output.

This program determines the cost of delivery

Please enter the weight of the package in lbs: 51

The package delivery for 51 lb package costs $ 14.49

Of that, $ 0.49 is charged as delivery tax.
"""

import math

print("This program determines the cost of delivery.")

flat_fee = 2
deliverytax = float(0.035)
costbyweight = 6
weight = int(input("Please enter the weight of the package in lbs: "))

#calculation
cost = costbyweight * math.floor(weight/25) + flat_fee
tax = deliverytax * cost
final_cost = cost + tax

formatted_cost = "${:,.2f}".format(final_cost)

formatted_tax = "${:,.2f}".format(tax)

print("The package delivery for a ", weight,"lbs package costs ", formatted_cost, "Of that, ", formatted_tax, "is charged as delivery tax.")
