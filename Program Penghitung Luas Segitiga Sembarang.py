def random_triangle_area(a, b, c) :
    if a <= 0 or b <= 0 or c <= 0 :
        print("These three sides can't make a triangle because one of them is 0 or less.")
    elif (a + b) <= c or (b + c) <= a or (a + c) <= b :
        print("These three sides can't make a triangle because one of the sides is bigger than or equal the two other sides combined.")
    else :
        s = a + b + c
        triangle_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"The area of the triangle made by these three sides is {triangle_area} unit.")

random_triangle_area(int(input("Enter the first side of the triangle = ")), int(input("Enter the second side of the triangle = ")), int(input("Enter the third side of the triangle = ")))

#done