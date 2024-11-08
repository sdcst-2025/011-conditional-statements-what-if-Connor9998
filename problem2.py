#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
a=input("Number:")
#convert to a number
a=float(a)
if int(a):
    print("the number is an integer")
elif (a) != int:
    print("this number is not a integer")