import math
integer = 0
while True:
    try:
      integer=float(input("what is length of a\n"))
      intege=float(input("what is the length of b\n"))
      if integer<0 or intege<0:
        print('please enter a positive number')
        continue
        
    except ValueError:
        print("Please enter a number")
        continue
      
    else:
        a=integer**2
        b=intege**2
        c2=a+b
        c=round(math.sqrt(c2),2)
        print("the hypotenuse of",integer,"and",intege,"is",c)
        break
