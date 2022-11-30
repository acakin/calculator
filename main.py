from replit import clear
from art import logo
def add(n1, n2):
  return n1 + n2
def subt(n1, n2):
  return n1 - n2
def mult(n1, n2):
  return n1 * n2
def div(n1, n2):
  return n1 / n2

operation = {
  "+" : add,
  "-" : subt,
  "*" : mult,
  "/" : div
}
def calc():
  print(logo)
  num1 = float(input("First number: "))
  for _ in operation:
      print(_)
  cont_calc = True
  while cont_calc:    
      op = input("Operation: ")
      num2 = float(input("Next number: "))
      calc_func = operation[op]
      ans = calc_func(num1, num2)
      print(f"{num1} {op} {num2} = {ans}")
      cont = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation.") 
      if cont =="y":
        num1 = ans
      else:
        cont_calc = False
        clear()
        calc()      
calc()  
               