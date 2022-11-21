import random
integer = 0
while True:
    try:
      integer=float(input("what is the min value\n"))
      intege=float(input("what is the max value\n"))
        
    except ValueError:
        print("Please enter a number")
        continue
      
    else:
        print(random.ranint(integer,intege))
        break