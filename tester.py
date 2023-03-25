import random as rd
import time
from typing import List, Tuple

from colorama import Fore, Style

from brute_force_bjk import brute_force
from upgrade_bf_bjk import *


def random_generator() -> Tuple[str, str]:
    alphabet = '()'
    
    a = b = ''
    
    size_a = rd.randint(10, 12)
    for _ in range(size_a):
        a += alphabet[rd.randint(0, 1)]
        
    size_b = rd.randint(10, 12)
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
            print(Fore.MAGENTA + chain[i], end = '')
        else:
            print(Style.RESET_ALL, end = '')
            print(chain[i], end = '')
    print('\n')


a, b = random_generator()
print(Fore.BLUE + a)
print()
print(Fore.RED + b)
print()


# brute force
start_bf = time.time()
result_bf = brute_force(a, b)
end_bf = time.time() - start_bf
print(Style.RESET_ALL, end = '')
print(len(result_bf[0]))
pretty_printing(result_bf[0], result_bf[1])
print(Style.RESET_ALL, end = '')
print('Time: ' + str(end_bf))


#upgraded brute force
start_ubf = time.time()
result_upgrade_bf = find_min_chain(a, b)
end_ubf = time.time() - start_ubf
print(Style.RESET_ALL, end = '')
print(len(result_upgrade_bf[0]))
pretty_printing(result_upgrade_bf[0], result_upgrade_bf[1])
print(Style.RESET_ALL, end = '')
print('Time: ' + str(end_ubf))
