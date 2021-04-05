# https://atcoder.jp/contests/abc108/submissions/21516595
# D - All Your Paths are Different Lengths
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l = int(input())
    n = l.bit_length()

    res = []
    ma = 0
    for i in range(n - 1):
        now, nxt = i + 1, i + 2
        cost = pow(2, i)
        res.append((now, nxt, 0))
        res.append((now, nxt, cost))
        ma += cost

    for i in range(n - 1):
        if l & (1 << i):
            now, nxt = i + 1, i + 2
            res.append((now, n, ma + 1))
            ma += pow(2, i)

    print(n, len(res))
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
