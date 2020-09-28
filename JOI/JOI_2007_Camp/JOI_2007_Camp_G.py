# https://atcoder.jp/contests/joisc2007/submissions/17078836
# anagram - アナグラム (Anagram)
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)
    D = Counter(S)

    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i)

    res = 1
    for i in range(n):
        small = 0
        dup = 1
        for k, v in D.items():
            if k < S[i]:
                small += v
            dup *= fact[v]
        res += small * fact[n - (i + 1)] // dup
        D[S[i]] -= 1
    print(res)


if __name__ == '__main__':
    resolve()
