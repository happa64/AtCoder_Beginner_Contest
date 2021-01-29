# https://atcoder.jp/contests/arc053/submissions/19748712
# C - 魔法使い高橋君
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    cool, heat = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        cool.append((a, b)) if a - b <= 0 else heat.append((a, b))

    cool.sort()
    heat.sort(key=lambda x: -x[1])

    res = now = 0
    for a, b in cool:
        res = max(res, now + a)
        now += a - b

    for a, b in heat:
        res = max(res, now + a)
        now += a - b
    print(res)


if __name__ == '__main__':
    resolve()
