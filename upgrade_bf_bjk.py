
from typing import List, Tuple

chains = []
colors = []

def upgrade_bf(a: str, b: str, current_chain: str, current_colors: List[int]) -> None:
    if len(a) == 0:
        chains.append(current_chain + b)
        for _ in b:
            current_colors.append(2)
        colors.append(current_colors)
        return
    if len(b) == 0:
        chains.append(current_chain + a)
        for _ in a:
            current_colors.append(1)
        colors.append(current_colors)
        return
    if a[0] == b[0]:
        upgrade_bf(a[1:], b[1:], current_chain + a[0], current_colors + [3])
    else:
        upgrade_bf(a[1:], b, current_chain + a[0], current_colors + [1])
        upgrade_bf(a, b[1:], current_chain + b[0], current_colors + [2])
        
def balance(chain: str) -> Tuple[str, int, int]:
    open = closed = 0
    for i in range(len(chain)):
        if chain[i] == '(':
            closed += 1
        else:
            closed -= 1
        if closed < 0:
            open += 1
            closed = 0
    open_list = ''.join(['(' for _ in range(open)])
    closed_list = ''.join([')' for _ in range(closed)])
    return open_list + chain + closed_list, open, closed

def find_min_chain_index(a: str, b: str) -> int:
    upgrade_bf(a, b, '', [])
    min_chain_i = 0
    min_chain_size = 10**10
    for i in range(len(chains)):
        chains[i], open, closed = balance(chains[i])
        colors[i] = [0 for _ in range(open)] + colors[i] + [0 for _ in range(closed)]
        if len(chains[i]) < min_chain_size:
            min_chain_i = i
            min_chain_size = len(chains[i])
    return min_chain_i
