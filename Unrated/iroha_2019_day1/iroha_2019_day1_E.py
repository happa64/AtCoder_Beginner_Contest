# https://atcoder.jp/contests/iroha2019-day1/submissions/18292221
# E - 放課後
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    section = []
    now = 0
    if b:
        D = list(map(int, input().split()))
        D.sort()
        for d in D:
            section.append(d - now - 1)
            now = d
    section.append(n - now)
    res = 0
    for s in section:
        q, r = divmod(s, a)
        res += q * (a - 1) + r
    print(res)


if __name__ == '__main__':
    resolve()
