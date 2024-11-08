#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
c=input("number")
#convet to a number
c= float(c)
if c > 0:
    print("positive")
elif c < 0:
    print("negative")
elif c == 0:
    print("zero")


