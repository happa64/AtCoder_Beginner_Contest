# https://atcoder.jp/contests/past202104-open/submissions/22052102
# C - 携帯電話の購入
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m = map(int, input().split())
    A = []
    for _ in range(n):
        k, *a = map(int, input().split())
        A.append(a)
    p, q = map(int, input().split())
    b = set(map(int, input().split()))

    res = 0
    for a in A:
        a = set(a)
        dup = (len(a) + len(b)) - len(a | b)
        if dup >= q:
            res += 1
    print(res)


if __name__ == '__main__':
    solve()
