from art import logo

#Add
def add(n1,n2):
  return n1 + n2

#Substract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  continue_calculation = True
  
  while continue_calculation:
    operations_symbol = input("Pick an operation: ")
    
    num2 = float(input("What's the next number?: "))
    
    # answer = operations[operations_symbol](num1,num2)
    
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
  
    calculate_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. And any other for exit: ")

      
    if calculate_again == 'y':
      num1 = answer
    elif calculate_again == 'n':
      continue_calculation = False
      calculator()
    else:
      continue_calculation = False
calculator()
