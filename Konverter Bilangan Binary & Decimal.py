def dec_to_bin(dec):
    if dec < 0: 
        print("Please enter a positive integer, at least 0.")

    elif dec == 0: 
        print(f"The binary form of {dec} is 0.")

    elif dec > 0:
        temporary_dec = dec
        power_of_2 = []
        bin = 0
        x = 0
        while 2**(x+1) <= dec:
            x += 1
        while temporary_dec > 0:
            if temporary_dec - 2**x >= 0:
                power_of_2.append(x)
                temporary_dec -= 2**x
            else:
                pass
            x -= 1
        for i in power_of_2:
            bin += 10**i
        print(f"The binary form of {dec} is {bin}.")

def bin_to_dec(bin):
    if set(bin) <= {"0", "1"}:
        temporary_bin = int(bin)
        power_of_2 = []
        dec = 0
        x = 0
        while 10**(x+1) <= int(bin):
            x += 1
        while temporary_bin > 0:
            if temporary_bin - 10**x >= 0:
                power_of_2.append(x)
                temporary_bin -= 10**x
            else:
                pass
            x -= 1
        for i in power_of_2:
            dec += 2**i
        print(f"The decimal form of {bin} is {dec}.")
    else:
        print(f"{bin} is not a valid positive binary number.")

restart = "y"

while restart.lower() == "y":
    print("Welcome to my binary, decimal and hexadecimal number converter!")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")

    opt = int(input("Please enter the option number: "))

    if opt == 1:
        dec_to_bin(int(input("Please enter a positive integer: ")))
    elif opt == 2:
        bin_to_dec(input("Please enter a positive binary number: "))
    else: 
        print("Invalid option number, please restart the program.")

    restart = input("Do you wanna restart the program? (y/n): ")