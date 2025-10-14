from math import gcd
from math import lcm

def gcd_num(numbers):
    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = gcd(gcd_result, num)
    return gcd_result

def lcm_num(numbers):
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

num_quantity = int(input("How many numbers you want to find the Greatest Common Divider & Least Common Multiply : "))
input_nums_list = []
for x in range(num_quantity):
    input_nums_list.append(int(input(f"Enter number {x+1}: ")))

print("The GCD of all numbers inputted is : ", gcd_num(input_nums_list))
print("The LCM of all numbers inputted is : ", lcm_num(input_nums_list))