import numpy as np
import math
import time
totimer1 = []
totimer2 = []
r = np.linspace(1,10000000,1)
for i in r:
    get = time.time()
    x = np.array([1,2,3,4,5,6])
    y = 187600000000000000005
    z = x*y
    stop = time.time()
    timer1 = (stop-get)
    totimer1.append([timer1])
    print(totimer1,z)
    arg = time.time()
    a = [1,2,3,4,5,6]
    b = 187600000000000000005
    c = [i * b for i in a]
    rag = time.time()   
    timer2 = (rag-arg)
    totimer2.append([timer2])
    print(totimer2,c)
    
print(totimer1.mean(),totimer2.mean())
