# https://atcoder.jp/contests/abc191/submissions/19955765
# B - Remove It
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    res = []
    for a in A:
        if a == x:
            continue
        res.append(a)
    print(*res)


if __name__ == '__main__':
    resolve()
