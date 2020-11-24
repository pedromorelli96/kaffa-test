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
# returns 1 if valid
# returns 0 if not valid
def validate_format(cnpj):
    answer = 0

    # Primary check : string size
    # if size == 14 : number only 
    # if size == 18 : formatted
    # else : incompatible
    if (len(cnpj) == 14):
        # Secondary check : numbers only
        if (cnpj.isdigit()):
            answer = 1
            
    elif (len(cnpj) == 18):
        # Secondary check :  
        # numbers and ./- allowed
        answer = 1

        # Splits the cnpj string using regular expression
        # Split parameters inside brackets are . / -
        temp = re.split("[./\\-]+", cnpj)

        # if temp size == 5 then
        # cnpj has adequate format separators
        if (len(temp) == 5):
            # Now to check if all other characters are numbers
            for section in temp:
                if not (section.isdigit()):
                    answer = 0
        else:
            answer = 0
            
    else:
        answer = 0

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





