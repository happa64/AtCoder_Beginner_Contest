# https://atcoder.jp/contests/code-festival-2018-final-open/submissions/16630839
# C - Telephone Charge
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
    m = int(input())
    T = sorted(list([i, int(input())] for i in range(m)), key=lambda x: x[1])

    res = [f_inf] * m
    i = 0
    for idx, t in T:
        while i < n and res[idx] > AB[i][1] + max(0, (t - AB[i][0])):
            a, b = AB[i]
            res[idx] = b + max(0, (t - a))
            i += 1
        i -= 1
        if i == n:
            a, b = AB[-1]
            res[idx] = b + max(0, (t - a))

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
