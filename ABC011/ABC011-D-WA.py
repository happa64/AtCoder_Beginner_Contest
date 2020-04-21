# https://atcoder.jp/contests/abc011/tasks/abc011_4
# D - 大ジャンプ(90点解法)
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d = map(int, input().split())
    x, y = map(int, input().split())

    if x % d or y % d:
        print(0)
        exit()

    cnt = 0
    # 4進法を使って全移動方法を試す
    for pattern in product([0, 1, 2, 3], repeat=n):
        next_x, next_y = 0, 0
        for i in pattern:
            if i == 0:
                next_x += d
            elif i == 1:
                next_x -= d
            elif i == 2:
                next_y += d
            else:
                next_y -= d

        if (next_x, next_y) == (x, y):
            cnt += 1

    res = cnt / (4 ** n)
    print(res)


if __name__ == '__main__':
    resolve()
