# https://atcoder.jp/contests/joi2013yo/submissions/15076072
# B - 数当てゲーム (Unique Number)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L1, L2, L3 = [], [], []
    for _ in range(n):
        a, b, c = map(int, input().split())
        L1.append(a)
        L2.append(b)
        L3.append(c)

    res = [0] * n
    for L in [L1, L2, L3]:
        for i in range(n):
            t = L[i]
            for j in range(n):
                if i == j:
                    continue
                s = L[j]
                if t == s:
                    break
            else:
                res[i] += L[i]
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
