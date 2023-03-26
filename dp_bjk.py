

from typing import List


def dynamic_solution(a: str, b: str) -> str:
    dp : List[List[List[int, List[List[int, int]]]]] = [[[0, [[0, 0], [0, 0], [0, 0]]] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        open_n = closed_n = 0
        balance_factor = 1
        if a[i - 1] == '(':
            closed_n = dp[i - 1][0][1][1][1] + balance_factor
        else:
            if dp[i - 1][0][1][1][1] > 0:
                balance_factor = - 1
                closed_n = dp[i - 1][0][1][1][1] + balance_factor
            else:
                open_n = dp[i - 1][0][1][1][0] + balance_factor
                
        cell = dp[i][0]
        cell[0] = dp[i - 1][0][0] + 1 + balance_factor
        cell[1][1] = [open_n, closed_n]
        
    for j in range(1, len(b) + 1):
        open_n = closed_n = 0
        balance_factor = 1
        if b[j - 1] == '(':
            closed_n = dp[0][j - 1][1][0][1] + balance_factor
        else:
            if dp[0][j - 1][1][0][1] > 0:
                balance_factor = - 1
                closed_n = dp[0][j - 1][1][0][1] + balance_factor
            else:
                open_n = dp[0][j - 1][1][0][0] + balance_factor
                
        cell = dp[0][j]
        cell[0] = dp[0][j - 1][0] + 1 + balance_factor
        cell[1][0] = [open_n, closed_n]
    
    
    # dir_r = [0, -1, -1]
    # dir_c = [-1, -1, 0]
    # for i in range(1, len(a) + 1):
    #     for j in range(1, len(b) + 1):
    #         if a[i - 1] == b[j - 1]:
    #             cell = dp[i][j]
    #             cell_poss_vals = [], open_n_poss_vals = [], closed_n_poss_vals = []
    #             for d in range(len(dir_r)):
    #                 previous_cell = dp[i + dir_r[d]][j + dir_c[d]]
    #                 for pill in previous_cell[1]:
    #                     prev_open_n = pill[0]
    #                     prev_closed_n = pill[1]
    #                     if a[i - 1] == '(':
    #                         cell_poss_vals.append(1 + previous_cell[0] + 1)
    #                         open_n_poss_vals.append()
        
    