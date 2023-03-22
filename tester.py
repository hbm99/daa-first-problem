import random as rd
from typing import List, Tuple
from brute_force_bjk import brute_force
from colorama import Fore, Style



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

def pretty_printing(chain: str, color_code: List[int]) -> None:
    for i in range(len(chain)):
        if color_code[i] == 1:
            print(Fore.BLUE + chain[i], end = '')
        elif color_code[i] == 2:
            print(Fore.RED + chain[i], end = '')
        elif color_code[i] == 3:
            print(Fore.GREEN + chain[i], end = '')
        else:
            print(Style.RESET_ALL, end = '')
            print(chain[i], end = '')
    print('\n')
            


a, b = random_generator()
print(Fore.BLUE + a)
print()
print(Fore.RED + b)
print()
result = brute_force(a, b)
pretty_printing(result[0], result[1])