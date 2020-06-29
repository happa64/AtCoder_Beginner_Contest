# https://atcoder.jp/contests/code-festival-2015-quala/submissions/13589473
# C - 8月31日
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]

    total = 0
    diff = []
    for a, b in AB:
        total += a
        diff.append(a - b)

    if total <= t:
        print(0)
    else:
        diff.sort(reverse=True)
        res = 0
        for i in range(n):
            res += 1
            total -= diff[i]
            if total <= t:
                print(res)
                break
        else:
            print(-1)


if __name__ == '__main__':
    resolve()
