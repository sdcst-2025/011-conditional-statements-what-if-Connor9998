#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
""""
input("number:")
input("number:")
input("number:")
"""

def is_right_triangle(a, b, c):
    
    sides = sorted([a, b, c])
    

    hypothesized_hypotenuse = sides[2]  
    side1, side2 = sides[0], sides[1]
    
    expected_hypotenuse = (side1**2 + side2**2) ** 0.5
    
    percent_diff = abs(expected_hypotenuse - hypothesized_hypotenuse) / hypothesized_hypotenuse * 100
    
    if percent_diff < 2:
        return "that is a right triangle"
    elif side1**2 + side2**2 > hypothesized_hypotenuse**2:
        return "that is an acute triangle"
    else:
        return "that is an obtuse triangle"


a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))


result = is_right_triangle(a, b, c)
print(result)
