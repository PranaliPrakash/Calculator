#Calculator
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2      

#Create a dictionary containing keys: symbols values : names of symbols
operations={ "+": add,
            "-" : sub,
            "*" : mul,
            "/": div
}
def calculator():
  from art import logo
  print(logo)

  num1= float(input("enter the 1st number:"))

  for keys in operations:
    print(keys)
  
  should_continue =True 
  while should_continue:
      operation_symbol= input("pick an operation from above:")
      function= operations[operation_symbol]
      num2= float(input("enter the next number:"))

      answer= function(num1,num2)

      print(f"{num1} {operation_symbol} {num2} = {answer}") 
      if input("do you want to continue:y or exit:n :") == "y":
        num1=answer
      else:
        should_continue=False 
        calculator() #recursion

calculator()        













