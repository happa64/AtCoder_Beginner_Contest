# https://atcoder.jp/contests/abc162/tasks/abc162_d
# D - RGB Triplets
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    r = s.count("R")
    g = s.count("G")
    b = s.count("B")

    # 条件を無視した全ての組み合わせの個数から、j - i != k - jとなる組み合わせの個数を引く
    res = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            # j - i = k - jをk = 2j - iに変形
            k = 2 * j - i
            if 1 <= k < n:
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    res -= 1

    print(res)


if __name__ == '__main__':
    resolve()
