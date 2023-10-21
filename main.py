from art import logo
import os
print(logo)

def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2
def remainder(n1,n2):
  return n1 % n2

operations = {
  '+':add ,
  '-':subtract,
  '*':multiply,
  '/':divide, 
  '%':remainder
}

def calculator():
  num1 = float(input('Whats the first number?: '))
  for symbol in operations:
    print(symbol)
      
  continueCalc = True
  while continueCalc:
    operation_symbol = input('Pick an operation: ')
    num2 = float(input('Whats the next number?: ')) 
    answer = operations[operation_symbol](num1,num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    num1 = answer
    should_continue = input(f"Would you like to continue calculating with {num1} type 'y' to continue and 'n' to start new equation: ").lower()
    
    if should_continue == 'n':
      continueCalc = False
      os.system('clear')
      calculator()
  
calculator()