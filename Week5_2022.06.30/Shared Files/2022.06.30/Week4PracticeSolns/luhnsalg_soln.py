"""
Luhn's Algorithm

Code adapted from:
https://pythoncircle.com/post/485/python-script-8-validating-credit-card-number-luhns-algorithm/

The Luhn algorithm, also known as the "modulus 10" algorithm,
is a checksum formula used to validate a variety of identification numbers,
such as credit card numbers, IMEI numbers, National Provider Identifier numbers
in the United States, Canadian Social Insurance Numbers and Israel ID Numbers.

Algorithm:
The formula verifies a number against its included check digit,
which is usually appended to a partial account number to generate the full account number.

Generating check digit:

Lets assume you have a number as: 3 - 7 - 5 - 6 - 2 - 1 - 9 - 8 - 6 - 7 - X where X is the check digit.
Now starting from the right most digit i.e. check digit, double every second digit.
New number will be: 3 - 14 - 5 - 12 - 2 - 2 - 9 - 16 - 6 - 14 - X

Now if double of a digit is more then 9, add the digits.
So the number will become: 3 - 5 - 5 - 3 - 2 - 2 - 9 - 7 - 6 - 5 - X

Now add all digits. 47 + X

Multiply the non-check part by 9. So it will be 47 * 9 = 423
Unit digit in the multiplication result is the check digit. X = 3

A valid number would be 37562198673.

Sample data: (from https://www.validcreditcardnumber.com/)
Credit Card 	Credit Card Number
Amer Express	371449635398431
Diners Club	    30569309025904
Discover	    6011111111111117
JCB	            3530111333300000
MasterCard	    5555555555554444
Visa	        4111111111111111
"""

def print_cc(message, cc):
    ## helping function to print a message followed by the cc num one digit at a time
    print(f"{message:25s}", end = "|")
    for d in cc:
        print(f"{d:>3}", end= "|")
    print()

def sum_digits(digit):
    # sum the digits of a two digit number
    if digit < 10:
        sum = digit
    else:
        sum = (digit % 10) + (digit // 10)
    return sum

def validate(cc_num):

    check_digit = int(cc_num[-1])  # last digit
    print_cc("Original", cc_num)
    working_digits = cc_num[::-1] # reverse the credit card number
    working_digits = [int(x) for x in working_digits]  # convert to a list of integers
    print_cc("Reversed", working_digits)

    for i in range(1, len(working_digits), 2):  #start at position 1 because 0 has check digit
        digit = working_digits[i]
        working_digits[i] = digit*2

    print_cc("Double every other", working_digits)

    for i in range(1, len(working_digits), 2):
        doubled_digit = working_digits[i]
        if doubled_digit >= 10:
            working_digits[i] = sum_digits(doubled_digit)

    print_cc("Add digits if >10", working_digits)

    sum_of_digits = sum(working_digits[1:])  #check digit is in position 0
    print("Sum Digits Except Check:", sum_of_digits, "Check Digit:", check_digit)

    # multiply by 9
    product = 9 * sum_of_digits
    print("Multiplied by 9 is", product, end = " ")

    # if the last digit of the product is the same as the check digit, it's valid
    if product % 10 == check_digit:
        result = True
    else:
        result = False
    print("Last digit of product is ", product % 10, "match = " , result)
    return result


def main():
    card_types = ['Example', 'American Express', 'Diners Club', 'Discover',
                  'JCB','MasterCard','Visa','Made This One Up']
    card_numbers = [ '37562198673',
                    "371449635398431","30569309025904","6011111111111117",
                   "3530111333300000","5555555555554444","4111111111111111",
                   "4111111111111112"]

    for i in range(len(card_types)):
        card_type = card_types[i]
        cc_num = card_numbers[i]
        print("Validating", card_type, "*"* 30)
        if validate(cc_num):
            print (f"{cc_num:16s} is a valid {card_type} credit card number.")
        else:
            print (f"{cc_num:16s} is not a valid {card_type} credit card number.")


main()
