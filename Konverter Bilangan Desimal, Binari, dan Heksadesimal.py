import time
import sys

def decimal_to_binary(dec_num) :
    bin_num = bin(dec_num).replace("0b", "")
    print(f"The binary form of {dec_num} is: {bin_num}")

def binary_to_decimal(bin_num) :
    bin_num = bin_num.lstrip("0") or "0"
    dec_num = int(bin_num, 2)
    print(f"The decimal form of {bin_num} is: {dec_num}")

def decimal_to_hexadecimal(dec_num) :
    hexadec_num = hex(dec_num).replace("0x", "").upper()
    print(f"The hexadecimal form of {dec_num} is: {hexadec_num}")

def hexadecimal_to_decimal(hexadec_num) :
    dec_num = int(hexadec_num, 16)
    print(f"The decimal form of {hexadec_num} is: {dec_num}")

def binary_to_hexadecimal(bin_num) :
    hexadec_num = hex(int(bin_num.lstrip("0") or "0", 2)).replace("0x", "").upper()
    print(f"The hexadecimal form of {bin_num} is: {hexadec_num}")

def hexadecimal_to_binary(hexadec_num) :
    bin_num = bin(int(hexadec_num, 16)).replace("0b", "")
    print(f"The binary form of {hexadec_num} is: {bin_num}")

def close_program() :
    print("Thanks for using this program! :)")
    sys.exit(0)

def ask_continue() :
    answer = input("Do you want to use the program again? (Y/N) : ").strip()
    if answer.lower() == "y":
        print("Loading...")
        time.sleep(2)
        return True
    elif answer.lower() == "n":
        close_program()
    else:
        print("You've entered an invalid option, the program will be closed soon.")
        time.sleep(2)
        close_program()

def main_program() :
    while True :
        print("Decimal, Binary and Hexadecimal Number Converter")
        print("Choose the option below :")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Decimal to Hexadecimal")
        print("4. Hexadecimal to Decimal")
        print("5. Binary to Hexadecimal")
        print("6. Hexadecimal to Binary")
        print("7. Exit")

        try:
            option = int(input("Enter the option number : "))
        except ValueError:
            print("Invalid input, please enter the option number available.")
            continue

        if option == 1:
            decimal_to_binary(int(input("Enter a decimal number: ")))
            ask_continue()
        elif option == 2:
            binary_to_decimal(input("Enter a binary number: "))
            ask_continue()
        elif option == 3:
            decimal_to_hexadecimal(int(input("Enter a decimal number: ")))
            ask_continue()
        elif option == 4:
            hexadecimal_to_decimal(input("Enter a hexadecimal number: "))
            ask_continue()
        elif option == 5:
            binary_to_hexadecimal(input("Enter a binary number: "))
            ask_continue()
        elif option == 6:
            hexadecimal_to_binary(input("Enter a hexadecimal number: "))
            ask_continue()
        elif option == 7:
            close_program()
        else:
            print("The option you entered isn't valid, please retry.")
            continue

        if not ask_continue:
            break

main_program()