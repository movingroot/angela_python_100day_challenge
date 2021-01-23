def prime_checker(num) :
  if num < 0 : 
    input("Please enter positive number. : ")
  elif num == 0 or num == 1 :
    input("Please enter number bigger than 2. : ")
  elif num == 2 or num == 3 :
    input(f"{num} is prime number.")
  else :
    is_prime = True
    div = num//2
    for i in range(2,div+1) :
      if num % i == 0 :
        is_prime = False
    
    if is_prime : print(f"{num} is prime number.")
    else : print(f"{num} is not a prime number.")
