def dec_to_bin(dec):
    bin_digits = "01"
    bin = ""
    if dec < 0:
        print("Please enter a positive integer, at least 0.")
    elif dec == 0:
        print(f"The binary form of {dec} is 0.")
    else:
        temporary_dec = dec
        while temporary_dec > 0:
            remainder = temporary_dec % 2
            bin = bin_digits[remainder] + bin
            temporary_dec //= 2
        print(f"The binary form of {dec} is {bin}.")

def bin_to_dec(bin):
    bin_digits = "01"
    valid_input = all(digit in bin_digits for digit in bin)
    if not valid_input or len(bin) == 0:
        print(f"{bin} is not a valid binary number.")
    else:
        dec = 0
        for digit in bin:
            value = bin_digits.index(digit)
            dec = dec * 2 + value
        print(f"The decimal form of {bin} is {dec}.")

def dec_to_oct(dec):
    oct_digits = "01234567"
    oct = ""
    if dec < 0:
        print("Please enter a positive integer, at least 0.")
    elif dec == 0: 
        print(f"The octal form of {dec} is 0.")
    else:
        temporary_dec = dec
        while temporary_dec > 0:
            remainder = temporary_dec % 8
            oct = oct_digits[remainder] + oct
            temporary_dec //= 8
        print(f"The octal form of {dec} is {oct}.")

def oct_to_dec(oct):
    oct_digits = "01234567"
    valid_input = all(digit in oct_digits for digit in oct)
    if not valid_input or len(oct) == 0:
        print(f"{oct} is not a valid binary number.")
    else:
        dec = 0
        for digit in oct:
            value = oct_digits.index(digit)
            dec = dec * 8 + value
        print(f"The decimal form of {oct} is {dec}.")

def dec_to_hexadec(dec):
    hexadec_digits = "0123456789ABCDEF"
    hexadec = ""
    if dec < 0:
        print("Please enter a positive integer, at least 0.")
    elif dec == 0: 
        print(f"The hexadecimal form of {dec} is 0.")
    else:
        temporary_dec = dec
        while temporary_dec > 0:
            remainder = temporary_dec % 16
            hexadec = hexadec_digits[remainder] + hexadec
            temporary_dec //= 16
        print(f"The hexadecimal form of {dec} is {hexadec}.")

def hexadec_to_dec(hexadec):
    hexadec = hexadec.upper()
    hexadec_digits = "0123456789ABCDEF"
    valid_input = all(ch in hexadec_digits for ch in hexadec)
    if not valid_input or len(hexadec) == 0:
        print(f"{hexadec} is not a valid hexadecimal number.")
    else:
        dec = 0
        for digit in hexadec:
            value = hexadec_digits.index(digit)
            dec = dec * 16 + value
        print(f"The decimal form of {hexadec} is {dec}.")

def bin_to_oct(bin):
    bin_digits = "01"
    oct_digits = "01234567"
    valid_input = all(digit in bin_digits for digit in bin)
    if not valid_input or len(bin) == 0:
        print(f"{bin} is not a valid positive binary number.")
    else:
        dec = 0
        oct = ""
        for digit in bin:
            dec = dec * 2 + bin_digits.index(digit)
        while dec > 0:
            remainder = dec % 8
            oct = oct_digits[remainder] + oct
            dec //= 8
        print(f"The octal form of {bin} is {oct}.")

def bin_to_hexadec(bin):
    bin_digits = "01"
    hexadec_digits = "0123456789ABCDEF"
    valid_input = all(digit in bin_digits for digit in bin)
    if not valid_input or len(bin) == 0:
        print(f"{bin} is not a valid positive binary number.")
    else:
        dec = 0
        hexadec = ""
        for digit in bin:
            dec = dec * 2 + bin_digits.index(digit)
        while dec > 0:
            remainder = dec % 16
            hexadec = hexadec_digits[remainder] + hexadec
            dec //= 16
        print(f"The hexadecimal form of {bin} is {hexadec}.")

def oct_to_bin(oct):
    bin_digits = "01"
    oct_digits = "01234567"
    valid_input = all(digit in oct_digits for digit in oct)
    if not valid_input or len(oct) == 0:
        print(f"{oct} is not a valid positive octal number.")
    else:
        dec = 0
        bin = ""
        for digit in oct:
            dec = dec * 8 + oct_digits.index(digit)
        while dec > 0:
            remainder = dec % 2
            bin = bin_digits[remainder] + bin
            dec //= 2
        print(f"The binary form of {oct} is {bin}.")

def oct_to_hexadec(oct):
    oct_digits = "01234567"
    hexadec_digits = "0123456789ABCDEF"
    valid_input = all(digit in oct_digits for digit in oct)
    if not valid_input or len(oct) == 0:
        print(f"{oct} is not a valid positive octal number.")
    else:
        dec = 0
        hexadec = ""
        for digit in oct:
            dec = dec * 8 + oct_digits.index(digit)
        while dec > 0:
            remainder = dec % 16
            hexadec = hexadec_digits[remainder] + hexadec
            dec //= 16
        print(f"The hexadecimal form of {oct} is {hexadec}.")

def hexadec_to_bin(hexadec):
    hexadec = hexadec.upper()
    bin_digits = "01"
    hexadec_digits = "0123456789ABCDEF"
    valid_input = all(digit in hexadec_digits for digit in hexadec)
    if not valid_input or len(hexadec) == 0:
        print(f"{hexadec} is not a valid positive hexadecimal number.")
    else:
        dec = 0
        bin = ""
        for digit in hexadec:
            dec = dec * 16 + hexadec_digits.index(digit)
        while dec > 0:
            remainder = dec % 2
            bin = bin_digits[remainder] + bin
            dec //= 2
        print(f"The binary form of {hexadec} is {bin}.")

def hexadec_to_oct(hexadec):
    hexadec = hexadec.upper()
    oct_digits = "01234567"
    hexadec_digits = "0123456789ABCDEF"
    valid_input = all(digit in hexadec_digits for digit in hexadec)
    if not valid_input or len(hexadec) == 0:
        print(f"{hexadec} is not a valid positive hexadecimal number.")
    else:
        dec = 0
        oct = ""
        for digit in hexadec:
            dec = dec * 16 + hexadec_digits.index(digit)
        while dec > 0:
            remainder = dec % 8
            oct = oct_digits[remainder] + oct
            dec //= 8
        print(f"The octal form of {hexadec} is {oct}.")

def dec_to_base25(dec):
    base25_digits = "0123456789ABCDEFGHIJKLMNO"
    base25 = ""
    if dec < 0:
        print("Please enter a positive integer, at least 0.")
    elif dec == 0: 
        print(f"The 25-base form of {dec} is 0.")
    else:
        temporary_dec = dec
        while temporary_dec > 0:
            remainder = temporary_dec % 25
            base25 = base25_digits[remainder] + base25
            temporary_dec //= 25
        print(f"The 25-base form of {dec} is {base25}.")

restart = "y"
while restart.lower() == "y":
    print("Welcome to my binary, decimal and hexadecimal number converter!")
    print("Choose the initial form of the input number.")
    print("1. Binary")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")

    first_opt = int(input("Please enter the option number: "))

    if first_opt == 1:
        input_bin = input("Please enter a positive binary number: ")
        bin_to_oct(input_bin)
        bin_to_dec(input_bin)
        bin_to_hexadec(input_bin)
    elif first_opt == 2:
        input_oct = input("Please enter a positive octal number: ")
        oct_to_bin(input_oct)
        oct_to_dec(input_oct)
        oct_to_hexadec(input_oct)
    elif first_opt == 3:
        input_dec = int(input("Please enter a positive integer: "))
        dec_to_bin(input_dec)
        dec_to_oct(input_dec)
        dec_to_hexadec(input_dec)
        dec_to_base25(input_dec)
    elif first_opt == 4:
        input_hexadec = input("Please enter a positive hexadecimal number: ")
        hexadec_to_bin(input_hexadec)
        hexadec_to_oct(input_hexadec)
        hexadec_to_dec(input_hexadec)
    else: 
        print("Invalid option number, please restart the program.")

    restart = input("Do you wanna restart the program? (y/n): ")