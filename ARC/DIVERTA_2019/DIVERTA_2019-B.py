# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b
# B - RGB Boxes
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    R, G, B, n = map(int, input().split())

    res = 0
    for r in range(n // R + 1):
        for g in range(n // G + 1):
            b = (n - (R * r + G * g)) // B
            if R * r + G * g + B * b == n and b >= 0:
                res += 1

    print(res)


if __name__ == '__main__':
    resolve()
