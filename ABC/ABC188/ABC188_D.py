# https://atcoder.jp/contests/abc188/submissions/19333699
# D - Snuke Prime
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(n)]

    event = []
    for a, b, c in ABC:
        event.append((a - 1, c))
        event.append((b, -c))
    event.sort()
    prev = event[0][0]
    tot = event[0][1]
    res = 0
    for now, c in event[1:]:
        t = now - prev
        if tot > C:
            res += C * t
        else:
            res += tot * t
        prev = now
        tot += c
    print(res)


if __name__ == '__main__':
    resolve()
