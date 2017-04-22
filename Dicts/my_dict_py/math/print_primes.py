import numpy as np

primes = []
times = []
start = time.time()
for num in range(10,20000):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         break
   else:                  # else part of the loop
      start = time.time()
      primes.append(num)
      stop = time.time()
      total = stop - start
      times.append(total)
      
print(primes)
print (np.mean(times))
