
import math
import numpy as np
from sympy import primefactors

a =[5,8,14]

def coprimes(a):
    return sum([math.gcd(a,el) == 1 for el in range(a)])

def cnt_coprimes_in_array(arr):
    return [coprimes(el) for el in arr]

a = np.random.randint(1000)
# print(a)
# print()
def coprimes_2(a):
    p_f = primefactors(a)
    ar = [(1-1/el) for el in p_f]
    num_coprimes = int(np.prod(ar) * a)
    return num_coprimes

# %%timeit
# print(cnt_coprimes_in_array(a))
res = coprimes_2(a)
# %%timeit
if  math.gcd(res,a) == 1:
        print("true")

print()
print(a)
print(res)