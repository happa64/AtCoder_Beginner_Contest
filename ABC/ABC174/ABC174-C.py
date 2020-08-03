# https://atcoder.jp/contests/abc174/submissions/15656158
# C - Repsept
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = f_inf


def resolve():
    k = int(input())
    x = 7 % k
    s = set()
    i = 1
    while x not in s:
        if x == 0:
            print(i)
            break
        s.add(x)
        x = (x * 10 + 7) % k
        i += 1
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
