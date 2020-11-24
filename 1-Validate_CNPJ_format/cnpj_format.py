#####################################################
# Kaffa - Pre-qualification Test
# 1) Validate CNPJ format (Mask)
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


# Reads string from stdin
cnpj = input()

# Calls validate_format function which returns
# adequate answer
answer = validate_format(cnpj)

# Simple output to stdout
if (answer):
    print(f"{cnpj} looks like a CNPJ")
else:
    print(f"{cnpj} does NOT look like a CNPJ")