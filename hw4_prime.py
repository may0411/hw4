def is_prime(num):
  root = int(num**0.5+1)
  if num <= 1:
    return False
  elif num == 2:
    return True
  else:
    for prime in range(2,root+1):
      n = 2
      while n <= root :
        n += 1
        if prime % n == 0:
          break
        else:  
          other_prime = prime
      if num % other_prime == 0:
        break
      else:
        return True 
      
      

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')
