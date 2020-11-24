#####################################################
# Kaffa - Pre-qualification Test
# 2) Validate CNPJ digits
# Name: Pedro Rodrigo Ramos Morelli
# E-mail: pedromorelli96@gmail.com
#####################################################

# Regular expression used to verify formatted string
import re

# Function that receives cnpj string to check if it is
# a valid format, returns correspondent answer code
# returns True if valid
# returns False if not valid
def validate_format(cnpj):
    answer = False

    # Primary check : string size
    # if size == 14 : number only 
    # else : has to be formatted
    if (len(cnpj) == 14):
        # Secondary check : numbers only
        if (cnpj.isdigit()):
            answer = True
            
    else:
        # Secondary check : correct format
        pattern = re.compile(r"^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$")
        # r makes python interpret regex syntax correctly
        # \d{n} checks for digits n times

        # Check if cnpj matches format
        if (pattern.match(cnpj)):
            answer = True

    return answer

# Function that receives cnpj string to check if it is
# a well-formed CNPJ
# returns True if well-formed, False otherwise
def validate_digits(cnpj):
    answer = False
    # First, we check if cnpj string looks like a CNPJ
    if not validate_format(cnpj):
        return False
    else:
        # Since we only care about the digits from now on
        # we need to convert the formatted cnpj string
        if (len(cnpj) > 14):
            removechar = "./-"
            for c in cnpj:
                if c in removechar:
                    cnpj = cnpj.replace(c, "")

        # There are many sources on the web detailing how to calculate
        # and determine if the verification digits on a CNPJ are correct
        # based on the remaining CNPJ numbers

        # Calculating first verification digit
        v1 = 5*int(cnpj[0]) + 4*int(cnpj[1]) + 3*int(cnpj[2]) + 2*int(cnpj[3])
        v1 += 9*int(cnpj[4]) + 8*int(cnpj[5]) + 7*int(cnpj[6]) + 6*int(cnpj[7])
        v1 += 5*int(cnpj[8]) + 4*int(cnpj[9]) + 3*int(cnpj[10]) + 2*int(cnpj[11])
        v1 = 11 - (v1 % 11)
        if (v1 >= 10):
            v1 = 0

        # Calculating second verification digit
        v2 = 6*int(cnpj[0]) + 5*int(cnpj[1]) + 4*int(cnpj[2]) + 3*int(cnpj[3])
        v2 += 2*int(cnpj[4]) + 9*int(cnpj[5]) + 8*int(cnpj[6]) + 7*int(cnpj[7])
        v2 += 6*int(cnpj[8]) + 5*int(cnpj[9]) + 4*int(cnpj[10]) + 3*int(cnpj[11])
        v2 += 2*int(cnpj[12])
        v2 = 11 - (v2 % 11)
        if (v2 >= 10):
            v2 = 0
    
        # Check if calculated verification digits are equal to those on provided CNPJ
        if (v1 == int(cnpj[12]) and v2 == int(cnpj[13])):
            answer = True

    return answer

# Reads string from stdin
cnpj = input()

# Calls validate_digits function which returns adequate answer
answer = validate_digits(cnpj)

# Simple output to stdout
if (answer):
    print(f"{cnpj} is a well-formed CNPJ")
else:
    print(f"{cnpj} is NOT a well-formed CNPJ")