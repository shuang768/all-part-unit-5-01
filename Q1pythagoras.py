import math
import random
def Q1():
  
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
def Q2():
  
  integer = 0
  while True:
    try:
      integer=float(input("what is the min value\n"))
      intege=float(input("what is the max value\n"))
        
    except ValueError:
        print("Please enter a number")
        continue
      
    else:
        print(random.randint(integer,intege))
        break
def Q3():
  
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


task=0
while True:
    try:
      print("which function do you want")
      print("1- Q1pythagoras")
      print("2- Q2randomrange")
      print("3- Q3addition")
      print("4- Q4picture")
      print("0- exit")
      task=int(input("enter your function "))

    except ValueError:
        print("Please enter a number")
        continue
      
    else:
      if task==1:
        Q1()
        break
      elif task==2:
        Q2()
        break
      elif task==3:
         Q3()
         break
      elif task==4:
          print("please check the other link")
          break
      elif task==0:
          print("exit")
          break
      else: 
        print("please enter a valid number")
        continue 