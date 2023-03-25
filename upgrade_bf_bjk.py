
from typing import List, Tuple

chains = []
colors = []

def upgrade_bf(a: str, b: str, current_chain: str, current_colors: List[int], open_n: int, closed_n: int) -> None:
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
        chains.append((current_chain + b, open_n, closed_n))
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
        chains.append((current_chain + a, open_n, closed_n))
        colors.append(current_colors)
        return
    if a[0] == b[0]:
        if a[0] == '(':
            upgrade_bf(a[1:], b[1:], current_chain + a[0], current_colors + [1], open_n, closed_n + 1)
        else:
            if closed_n > 0:
                upgrade_bf(a[1:], b[1:], current_chain + a[0], current_colors + [3], open_n, closed_n - 1)
            else:
                upgrade_bf(a[1:], b[1:], current_chain + a[0], current_colors + [3], open_n + 1, closed_n)
    else:
        if a[0] == '(':
            upgrade_bf(a[1:], b, current_chain + a[0], current_colors + [1], open_n, closed_n + 1)
        else:
            if closed_n > 0:
                upgrade_bf(a[1:], b, current_chain + a[0], current_colors + [1], open_n, closed_n - 1)
            else:
                upgrade_bf(a[1:], b, current_chain + a[0], current_colors + [1], open_n + 1, closed_n)
        if b[0] == '(':
            upgrade_bf(a, b[1:], current_chain + b[0], current_colors + [2], open_n, closed_n + 1)
        else:
            if closed_n > 0:
                upgrade_bf(a, b[1:], current_chain + b[0], current_colors + [2], open_n, closed_n - 1)
            else:
                upgrade_bf(a, b[1:], current_chain + b[0], current_colors + [2], open_n + 1, closed_n)

def find_min_chain(a: str, b: str) -> int:
    upgrade_bf(a, b, '', [], 0, 0)
    min_to_balance = min(chains, key=lambda x: len(x[0]) + x[1] + x[2])
    i = chains.index(min_to_balance)
    min_chain = ''.join(['(' for _ in range(min_to_balance[1])]) + min_to_balance[0] + ''.join([')' for _ in range(min_to_balance[2])])
    min_chain_colors = [0 for _ in range(min_to_balance[1])] + colors[i] + [0 for _ in range(min_to_balance[2])]
    return min_chain, min_chain_colors
