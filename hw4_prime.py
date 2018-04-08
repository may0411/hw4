def is_prime(num):
  root = int(num**0.5+1)
  if num <= 1:
    return False
  elif num == 2:
    return True
  else:
    for prime in range(2,root):
      for i in range(2,prime):
        if prime % i == 0:
          break
      prime2 = prime
      if num % prime2 == 0:
        return False
        break
    else:
      return True 
          

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')
