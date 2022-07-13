"""
2. New This Week: Luhn’s Algorithm.

The Luhn algorithm, also known as the "modulus 10" algorithm, is a checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers in the United States, Canadian Social Insurance Numbers and Israel ID Numbers. Algorithm: The formula verifies a number against its included check digit, which is usually appended to a partial account number to generate the full account number.

Original Credit Card Number 3 - 7 - 5 - 6 - 2 - 1 - 9 - 8 - 6 - 7 - X

Start from the right, and double every second digit 3 - 14 - 5 - 12 - 2 - 2 - 9 - 16 - 6 - 14 - X

If any doubled result is 10 or more, add those digits 3 - 5 - 5 - 3 - 2 - 2 - 9 - 7 - 6 - 5 - X

Add all the digits 47 + X

Multiply the non-check digit part by 9 47 * 9 = 423

The check digit is the unit’s digit in the result. 3

A valid credit card number is 37562198673

Sample data: (from https://www.validcreditcardnumber.com/) Feel free to test this algorithm personally by adding data from one of your credit cards (don’t put that in the video though!)

Write a function called validate (cc_num) which validates a credit card number using the algorithm above. It should work with this main driver function.
"""

# Original_Credit_Card_Number = input("")

def main():
    card_types = ['American Express', 'Diners Club', 'Discover',
                          'JCB','MasterCard','Visa','Made This One Up']

    card_numbers = ["371449635398431","30569309025904","6011111111111117",
                    "3530111333300000","5555555555554444","4111111111111111",
                    "4111111111111112"]

    for i in range(len(card_types)):
        card_type = card_types[i]
        cc_num = card_numbers[i]
        if validate(cc_num): # Boolean Function!!! Because if True..., else...
            print (f"{cc_num:16s} is a valid {card_type} credit card number.")

        else: print (f"{cc_num:16s} is not a valid {card_type} credit card number.")


# algorithm that validates a credit card number
def validate(cc_num):
    check_digit = int(cc_num[-1])
    cc_num_process = cc_num[:-1]
    validation = []
    number = '1234567890'
    last_digit = len(cc_num_process)-1
    i = 0
    n = 0
    sum_validation = 0

    # to get last number
    for _ in cc_num_process:
        if len(cc_num_process)%2 == 0:
            # EVEN TOTAL NUMBERS: double every second digit starting from the right
            if i%2 == 0:
                validation.append(int(cc_num_process[i]))
                i+=1
            else:
                validation.append(int(cc_num_process[i])*2)
                i+=1

        else:
            # ODD TOTAL NUMBERS: double every second digit starting from the right
            if i%2 == 0:
                validation.append(int(cc_num_process[i])*2)
                i+=1
            else:
                validation.append(int(cc_num_process[i]))
                i+=1

        # output = [3, 14, 5, 12, 2, 2, 9, 16, 6, 14]


    for digit in validation:
        if digit//10 == 1:
            # ten digit + unit digit
            validation[n] = (digit//10)+(digit%10)
            n+=1

        else:
            n+=1

        # output = [3, 5, 5, 3, 2, 2, 9, 7, 6, 5]

    # SUM all digits
    for element in range(len(validation)):  # range(len(validation))=range(0, 10)
        sum_validation = sum_validation + validation[element]

    # Multiply the non-check digit part by 9
    # The check digit is the unit’s digit in the result
    non_check_digit = sum_validation*9%10 # non_check_digit=3
    validation.append(non_check_digit)

    # output = [3, 5, 5, 3, 2, 2, 9, 7, 6, 5, 3]

    # return validation
    if check_digit == non_check_digit:
        return True
    else:
        return False


main()
