# Your task in this kata is to implement a function that calculates the sum of the integers inside
# a string.For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog",
# the sum of the integers is 3635.

def sum_of_int_in_a_str(str):
    sum_digits = 0
    for x in str:
        if x.isdigit() == True:
            digit = int(x)
            sum_digits = sum_digits + digit
    return sum_digits
