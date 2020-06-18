# https://atcoder.jp/contests/arc005/submissions/13109406
# B - P-CASカードと高橋君
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y, w = map(lambda z: int(z) - 1 if z.isdigit() else str(z), input().split())
    C = [list(input()) for _ in range(9)]

    dx, dy = (1, 0) if w == "R" else (-1, 0) if w == "L" else (0, 1) if w == "D" else (0, -1) if w == "U" else \
             (1, -1) if w == "RU" else (1, 1) if w == "RD" else (-1, -1) if w == "LU" else (-1, 1)

    res = ""
    for i in range(4):
        res += str(C[y][x])
        if x + dx < 0 or x + dx > 8:
            dx *= -1
        if y + dy < 0 or y + dy > 8:
            dy *= -1
        x += dx
        y += dy

    print(res)


if __name__ == '__main__':
    resolve()
