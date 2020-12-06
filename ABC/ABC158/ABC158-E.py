# https://atcoder.jp/contests/abc158/submissions/18607645
# E - Divisible Substring
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def debug(n, p, S):
    res = 0
    for i in range(n):
        s = ""
        for j in range(i, n):
            s += S[j]
            if int(s) % p == 0:
                res += 1
    return res


def resolve():
    n, p = map(int, input().split())
    S = input()
    res = 0

    if p == 2 or p == 5:
        for i in range(n):
            if int(S[i]) % p == 0:
                res += i + 1
    else:
        S_mod = []
        for i in range(n):
            S_mod.append(int(S[i]) * pow(10, n - (i + 1), p) % p)

        S_mod_acc = [0]
        for i in range(n):
            nxt = (S_mod_acc[-1] + S_mod[i]) % p
            S_mod_acc.append(nxt)

        D = Counter(S_mod_acc)
        for v in D.values():
            res += v * (v - 1) // 2

    print(res)
    # print(debug(n, p, S))


if __name__ == '__main__':
    resolve()
