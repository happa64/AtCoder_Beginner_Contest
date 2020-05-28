# https://atcoder.jp/contests/past202004-open/tasks/past202004_d
# D - パターンマッチ
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)
    S = ["."] + list(set(s))

    P = []
    # 全てのパターンを生成する
    for i in range(1, 4):
        for pattern in product(S, repeat=i):
            pattern = "".join(pattern)
            P.append(pattern)

    res = 0
    for p in P:
        if len(p) <= n:
            for i in range(n):
                if i + len(p) <= n:
                    ss = s[i: i + len(p)]
                    for j in range(len(p)):
                        if p[j] != ss[j] and p[j] != ".":
                            break
                    else:
                        res += 1
                        break

    print(res)


if __name__ == '__main__':
    resolve()
