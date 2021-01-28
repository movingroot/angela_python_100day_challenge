def try_again(_result) :
  str = input(f"Type 'y' to continue calculating with {_result}, or type 'n' to start a new calculation: ")
  if str == 'y' :
    print(f"First number : {_result}")
    calculating(_result)
  elif str == 'n' :
    _first = input("What is your first number? : ")
    calculating(_first)

def calculating(initial) :
  operations = ['+', '-', '*', '/']
  for i in range(0, len(operations)) :
    print(operations[i])
  operation = input("Pick an operation : ")
  to_cal = input("What's the next number? : ")

  if operation == operations[0] :
    result = int(initial) + int(to_cal)
    print(f"{initial} + {to_cal} = {result}")
  elif operation == operations[1] :
    result = int(initial) - int(to_cal)
    print(f"{initial} - {to_cal} = {result}")
  elif operation == operations[2] :
    result = int(initial) * int(to_cal)
    print(f"{initial} * {to_cal} = {result}")
  else :
    result = int(initial) // int(to_cal)
    print(f"{initial} / {to_cal} = {result}")
  
  try_again(result)


first_num = input("What is your first number? : ")
calculating(first_num)
