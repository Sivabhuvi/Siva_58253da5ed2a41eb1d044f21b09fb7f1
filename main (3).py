length = int(input("What is the length of the rectangle in cm?"'\n'))
width = float(input("What is the width of the rectanglein cm?"'\n'))
hi = input(str("Would you like to know the perimeter or area of the rectangle, please enter a or p"'\n'))
if hi == "a":
  area = length* width
  print ("The area of your rectangle is",area)
elif hi == "p":
  perimeter = length *2 + width *2
  print ("The area of your rectangle is",perimeter)