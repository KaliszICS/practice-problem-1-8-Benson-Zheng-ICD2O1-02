
def q1():
  #Write Assignment code here
 bool1 = True
 bool2 = False
 print(bool1 and bool2)
 print(bool1 or bool2)

def q2():
  #Write Assignment code here
  ink = int(input("Enter an integer: "))

  bum = ink != 0

  print(bum)



def q3():
  #Write Assignment code here
  input1 = input("Enter a number: ")
  number = float(input1)
  onetoten = (0 <= number <= 10)
  print(onetoten)
  

def q4():
  #Write Assignment code here
  food1 = input("Input food: ")
  drink1 = input("Input drink: ")
  pizza = "pizza"
  pop = "pop"
  fart = food1 == pizza and drink1 == pop
  print(not(fart))


def q5():
  #Write Assignment code here
  user_input = input("Enter an integer: ")
  int1 = int(user_input)
  CheckDivide2 = int1 % 2 == 0
  print(f"The integer {int1} is {(CheckDivide2)}.")
  

#Do not edit code after this
#Comment out the following code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
