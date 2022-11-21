import random
a=random.randint(1,100)
b=random.randint(1,100)
c=a+b
integer = 0
while True:
    try:
      print(a,"+",b)
      integer=int(input("what is the answer\n"))
        
    except ValueError:
        print("Please enter a number")
        continue
      
    else:
        if integer==c:
          print("correct")
        else: 
          print("wrong answer, the answer is ",c)
        break
