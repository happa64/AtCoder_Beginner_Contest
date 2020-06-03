# https://atcoder.jp/contests/agc011/tasks/agc011_a
# A - Airport Bus
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c, k = map(int, input().split())
    T = sorted(list(int(input()) for _ in range(n)))
    res = 0
    cnt = 0
    dep = T[0] + k
    for i in range(n):
        if cnt == c or T[i] > dep:
            res += 1
            cnt = 1
            dep = T[i] + k
        else:
            cnt += 1

    print(res + 1)


if __name__ == '__main__':
    resolve()
