# Add
def add(n1, n2):
   return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operations_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operations_symbol]
answer = calculation_function(num1, num2)
        
print(f"{num1} {operations_symbol} {num2} = {answer}")