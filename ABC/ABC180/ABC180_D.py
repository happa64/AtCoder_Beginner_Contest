# https://atcoder.jp/contests/abc180/submissions/17447451
# D - Takahashi Unevolved
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y, a, b = map(int, input().split())

    res = 0
    while x < y:
        if x * a - x < b:
            if y <= a * x:
                break
            else:
                res += 1
                x *= a
        else:
            res += (y - x - 1) // b
            break
    print(res)


if __name__ == '__main__':
    resolve()
