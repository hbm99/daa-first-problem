import random as rd
import time
from typing import List, Tuple

from colorama import Fore, Style

from brute_force_bjk import brute_force
from dp_bjk import dp_bjk
from upgrade_bf_bjk import *


def random_generator() -> Tuple[str, str]:
    
    alphabet = '()'
    a = b = ''
    
    size_a = rd.randint(1, 600)
    open_count = closed_count = 0
    for _ in range(size_a):
        number = rd.randint(0, 1)
        open_count += 1 if number == 0 else open_count
        closed_count += 1 if number == 1 else closed_count
        if open_count == 300 or closed_count == 300:
            break
        a += alphabet[number]
        
    size_b = rd.randint(1, 600)
    open_count = closed_count = 0
    for _ in range(size_b):
        number = rd.randint(0, 1)
        open_count += 1 if number == 0 else open_count
        closed_count += 1 if number == 1 else closed_count
        if open_count == 300 or closed_count == 300:
            break
        b += alphabet[number]
    
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
""" start_bf = time.time()
result_bf = brute_force(a, b)
end_bf = time.time() - start_bf
print(Style.RESET_ALL, end = '')
print(len(result_bf[0]))
pretty_printing(result_bf[0], result_bf[1])
print(Style.RESET_ALL, end = '')
print('Time: ' + str(end_bf)) """


# upgraded brute force oc
""" start_ubf = time.time()
result_upgrade_bf_oc = find_min_chain_oc(a, b)
end_ubf = time.time() - start_ubf
print(Style.RESET_ALL, end = '')
print(len(result_upgrade_bf_oc[0]))
pretty_printing(result_upgrade_bf_oc[0], result_upgrade_bf_oc[1])
print(Style.RESET_ALL, end = '')
print('Time: ' + str(end_ubf)) """

# upgraded brute force bf
""" start_ubf = time.time()
result_upgrade_bf_balance = find_min_chain_balance_f(a, b)
end_ubf = time.time() - start_ubf
print(Style.RESET_ALL, end = '')
print(len(result_upgrade_bf_balance))
print(result_upgrade_bf_balance)
print(Style.RESET_ALL, end = '')
print('Time: ' + str(end_ubf)) """


# dynamic programming
start_ubf = time.time()
chain = dp_bjk(a, b)
end_ubf = time.time() - start_ubf
print(len(chain))
print(Style.RESET_ALL, end = '')
print(chain)
print('Time: ' + str(end_ubf))


# To test all solutions uncomment previous method calls (block comments) 
# and uncomment next solution sizes comparisons
# Before testing this, it is recommended to change the chains possible top size at the random generator

""" equal_solution_sizes = len(chain) == len(result_upgrade_bf_oc[0]) == len(result_upgrade_bf_balance) == len(result_bf[0])
if equal_solution_sizes:
    print(Fore.GREEN + str(equal_solution_sizes))
else:
    print(Fore.RED + str(equal_solution_sizes)) """
