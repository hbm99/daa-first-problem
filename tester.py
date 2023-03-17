import random as rd
from typing import Tuple
from brute_force_bjk import brute_force


def random_generator() -> Tuple[str, str]:
    alphabet = '()'
    
    a = b = ''
    
    size_a = rd.randint(1, 10)
    for _ in range(size_a):
        a += alphabet[rd.randint(0, 1)]
        
    size_b = rd.randint(1, 10)
    for _ in range(size_b):
        b += alphabet[rd.randint(0, 1)]
    
    return a, b


a, b = random_generator()
print(a)
print()
print(b)
print()
print(brute_force(a, b))