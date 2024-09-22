def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Zero division error"

def calculator():
    print("CHOOSE ONE OPTION")
    print("1.SUM")
    print("2.SUBRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    
    while True:
      choice=input("enter the choice:(1,2,3,4)")
      if choice in ["1","2","3","4"]:
          try:
              num1=float(input("enter the num"))
              num2=float(input("enter the num"))
          except ValueError:
              print("input is invalid, enter the correct value")
              continue
          if choice=="1":
                print(f"the output is {add(num1,num2)}")
          elif choice=="2":
                print(f"the output is {sub(num1,num2)}")
          elif choice=="3":
                print(f"the output is {multiply(num1,num2)}")
          elif choice=="4":
                print(f"the output is {divide(num1,num2)}")
          else:
               print("invalid input")

      nextcalculation=input("enter the choice(yes/no)")
      if nextcalculation.lower()!="yes":
          break

calculator()
