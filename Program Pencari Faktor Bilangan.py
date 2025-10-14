def find_factor(x) :
    if x < 1 :
        print("Input invalid, please restart the program and enter a natural number.")
    else:
        i = 1
        factor = []
        while i <= x :
            if x % i == 0:
                factor.append(i)
                i += 1
            else:
                i += 1
                continue
        if factor.__len__ == 1:
            print(f"The factor of number {x} is {factor}")
        else:
            print(f"The factors of number {x} are {factor}")

find_factor(int(input("Enter a natural number (1, 2, 3, ...) : ")))