
from __future__ import annotations

from typing import List

MAX_VALUE = 10**10

def dp_bjk(a: str, b: str) -> str:
    dp : List[List[List[int]]] = [[[MAX_VALUE] * (len(a) + len(b) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    
    dp[0][0][0] = 0
    
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            for k in range(len(dp[i][j]) - 1):
                if i < len(a):
                    value = 0
                    if a[i] == '(':
                        value = 1
                    else: value = -1
                    bf = k + value
                    if bf < 0:
                        dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k] + 2)
                    else:
                        dp[i + 1][j][bf] = min(dp[i + 1][j][bf], dp[i][j][k] + 1)
                if j < len(b):
                    if b[j] == '(':
                        value = 1
                    else: value = -1
                    bf = k + value
                    if bf < 0:
                        dp[i][j + 1][k] = min(dp[i][j + 1][k], dp[i][j][k] + 2)
                    else:
                        dp[i][j + 1][bf] = min(dp[i][j + 1][bf], dp[i][j][k] + 1)
                if i < len(a) and j < len(b):
                    if a[i] == b[j]:
                        if bf < 0:
                            dp[i + 1][j + 1][k] = min(dp[i + 1][j + 1][k], dp[i][j][k] + 2)
                        else:
                            dp[i + 1][j + 1][bf] = min(dp[i + 1][j + 1][bf], dp[i][j][k] + 1)
                            
                            
    k = find_best_length(dp, len(a), len(b), len(dp[0][0]))
    
    chain = ''.join(build_chain(a, b, dp, k))
            
    return chain[::-1]

def build_chain(a : str, b: str, dp: List[List[List[int]]], k: int) -> List[str]:
    i, j = len(a), len(b)
    chain = [')'] * k
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1]:
            val = 1 if a[i - 1] == '(' else -1
            if dp[i - 1][j - 1][k - val] + 1 == dp[i][j][k]:
                chain.append(a[i - 1])
                k -= val
                i -= 1
                j -= 1
                continue
            elif k == 0 and a[i - 1] == ')' and dp[i - 1][j - 1][k] + 2 == dp[i][j][k]:
                chain.extend((')', '('))
                i -= 1
                j -= 1
                continue
        if i > 0:
            val = 1 if a[i - 1] == '(' else -1
            if dp[i - 1][j][k - val] + 1 == dp[i][j][k]:
                chain.append(a[i - 1])
                k -= val
                i -= 1
                continue
            elif k == 0 and a[i - 1] == ')' and dp[i - 1][j][k] + 2 == dp[i][j][k]:
                chain.extend((')', '('))
                i -= 1
                continue
        if j > 0:
            val = 1 if b[j - 1] == '(' else -1
            if dp[i][j - 1][k - val] + 1 == dp[i][j][k]:
                chain.append(b[j - 1])
                k -= val
                j -= 1
                continue
            elif k == 0 and b[j - 1] == ')' and dp[i][j - 1][k] + 2 == dp[i][j][k]:
                chain.extend((')', '('))
                j -= 1
                continue
    return chain

def find_best_length(dp, len_a: int, len_b: int, deep_length: int) -> int:
    index = 0
    best_length = MAX_VALUE
    for i in range(deep_length):
        if dp[len_a][len_b][i] + i < best_length:
            best_length = dp[len_a][len_b][i] + i
            index = i
    return index



    