# https://atcoder.jp/contests/abc091/submissions/12986870
# B - Two Colors Card Game
import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = [input() for _ in range(n)]
    m = int(input())
    T = [input() for _ in range(m)]

    D_S = Counter(S)
    D_T = Counter(T)
    res = 0
    for k, v in D_S.items():
        cnt = v - D_T.get(k, 0)
        res = max(res, cnt)

    print(res)


if __name__ == '__main__':
    resolve()
