# https://atcoder.jp/contests/abc009/submissions/19577589
# C - 辞書式順序ふたたび
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    S = list(input())
    S_sort = sorted(S)

    res = [""] * n
    for i in range(n):
        for j in range(len(S_sort)):
            res[i] = S_sort[j]
            D = Counter(S)
            cnt = 0
            for s, t in zip(S, res):
                if s == t:
                    D[t] -= 1
                elif t != "":
                    cnt += 1
                    D[t] -= 1
                else:
                    if D[s] >= 1:
                        D[s] -= 1
                    else:
                        cnt += 1
            if cnt <= k:
                S_sort.pop(j)
                break
    print("".join(res))


if __name__ == '__main__':
    resolve()
