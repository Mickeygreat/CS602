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

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(cc_num):

    check_digit = int(cc_num[-1])  # last digit

    cc_num = cc_num[::-1] # reverse the credit card number
    cc_num = [int(x) for x in cc_num]  # convert to a list of integers

    doubled_second_digit_list = []     # double every second digit
    digits = list(enumerate(cc_num, start=1))
    # print(digits)  # good example of enumerate

    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]

    # sum all digits
    # skip the check digit in the sum
    sum_of_digits = sum(doubled_second_digit_list[1:])

    # multiply by 9
    product = 9 * sum_of_digits

    # if the last digit of the product is the same as the check digit, it's valid
    if product % 10 == check_digit:
        result = True
    else:
        result = False

    return result


def main():
    test_cc_nums = {"American Express":	"371449635398431",
                    "Diners Club": "30569309025904",
                    "Discover": "6011111111111117",
                    "JCB":"3530111333300000",
                    "MasterCard":"5555555555554444",
                    "Visa":	"4111111111111111",
                    "Made This One Up":"4111111111111112"}

    for card_type, cc_num in test_cc_nums.items():
        if validate(cc_num):
            print (f"{cc_num:16s} is a valid {card_type} credit card number.")
        else:
            print (f"{cc_num:16s} is not a valid {card_type} credit card number.")


main()
