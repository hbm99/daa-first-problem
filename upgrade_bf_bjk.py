
from typing import List

chains_oc = []
chains_bf = []
colors = []

# Recursive solution counting open and closed parenthesis needed
def open_closed_bf(a: str, b: str, current_chain: str, current_colors: List[int], open_n: int, closed_n: int) -> None:
    if len(a) == 0:
        for item in b:
            if item == '(':
                closed_n += 1
            else:
                if closed_n > 0:
                    closed_n -= 1
                else:
                    open_n += 1
            current_colors.append(2)
        chains_oc.append((current_chain + b, open_n, closed_n))
        colors.append(current_colors)
        return
    if len(b) == 0:
        for item in a:
            if item == '(':
                closed_n += 1
            else:
                if closed_n > 0:
                    closed_n -= 1
                else:
                    open_n += 1
            current_colors.append(1)
        chains_oc.append((current_chain + a, open_n, closed_n))
        colors.append(current_colors)
        return
    if a[0] == b[0]:
        if a[0] == '(':
            open_closed_bf(a[1:], b[1:], current_chain + a[0], current_colors + [1], open_n, closed_n + 1)
        else:
            if closed_n > 0:
                open_closed_bf(a[1:], b[1:], current_chain + a[0], current_colors + [3], open_n, closed_n - 1)
            else:
                open_closed_bf(a[1:], b[1:], current_chain + a[0], current_colors + [3], open_n + 1, closed_n)
    else:
        if a[0] == '(':
            open_closed_bf(a[1:], b, current_chain + a[0], current_colors + [1], open_n, closed_n + 1)
        else:
            if closed_n > 0:
                open_closed_bf(a[1:], b, current_chain + a[0], current_colors + [1], open_n, closed_n - 1)
            else:
                open_closed_bf(a[1:], b, current_chain + a[0], current_colors + [1], open_n + 1, closed_n)
        if b[0] == '(':
            open_closed_bf(a, b[1:], current_chain + b[0], current_colors + [2], open_n, closed_n + 1)
        else:
            if closed_n > 0:
                open_closed_bf(a, b[1:], current_chain + b[0], current_colors + [2], open_n, closed_n - 1)
            else:
                open_closed_bf(a, b[1:], current_chain + b[0], current_colors + [2], open_n + 1, closed_n)

def find_min_chain_oc(a: str, b: str) -> int:
    open_closed_bf(a, b, '', [], 0, 0)
    min_to_balance = min(chains_oc, key=lambda x: len(x[0]) + x[1] + x[2])
    i = chains_oc.index(min_to_balance)
    min_chain = ''.join(['(' for _ in range(min_to_balance[1])]) + min_to_balance[0] + ''.join([')' for _ in range(min_to_balance[2])])
    min_chain_colors = [0 for _ in range(min_to_balance[1])] + colors[i] + [0 for _ in range(min_to_balance[2])]
    return min_chain, min_chain_colors


# Balance factor recursive solution 
def balance_factor_bf(a: str, b: str, current_chain: str, balance_f: int) -> None:
    if len(a) == 0:
        for item in b:
            if item == '(':
                balance_f += 1
                current_chain += '('
            else:
                if balance_f > 0:
                    balance_f -= 1
                    current_chain += ')'
                else:
                    current_chain += '()'
        chains_bf.append((current_chain, balance_f))
        return
    if len(b) == 0:
        for item in a:
            if item == '(':
                balance_f += 1
                current_chain += '('
            else:
                if balance_f > 0:
                    balance_f -= 1
                    current_chain += ')'
                else:
                    current_chain += '()'
        chains_bf.append((current_chain, balance_f))
        return
    if a[0] == b[0]:
        if a[0] == '(':
            balance_factor_bf(a[1:], b[1:], current_chain + a[0], balance_f + 1)
        else:
            if balance_f > 0:
                balance_factor_bf(a[1:], b[1:], current_chain + a[0], balance_f - 1)
            else:
                balance_factor_bf(a[1:], b[1:], current_chain + '(' + a[0], balance_f)
    else:
        if a[0] == '(':
            balance_factor_bf(a[1:], b, current_chain + a[0], balance_f + 1)
        else:
            if balance_f > 0:
                balance_factor_bf(a[1:], b, current_chain + a[0], balance_f - 1)
            else:
                balance_factor_bf(a[1:], b, current_chain + '(' + a[0], balance_f)
        if b[0] == '(':
            balance_factor_bf(a, b[1:], current_chain + b[0], balance_f + 1)
        else:
            if balance_f > 0:
                balance_factor_bf(a, b[1:], current_chain + b[0], balance_f - 1)
            else:
                balance_factor_bf(a, b[1:], current_chain + '(' + b[0], balance_f)
                
def find_min_chain_balance_f(a: str, b: str) -> int:
    balance_factor_bf(a, b, '', 0)
    min_to_balance = min(chains_bf, key=lambda x: len(x[0]) + x[1])
    min_chain = min_to_balance[0] + ''.join([')' for _ in range(min_to_balance[1])])
    return min_chain
