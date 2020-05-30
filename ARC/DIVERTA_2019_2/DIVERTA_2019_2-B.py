# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_b
# B - Picking Up
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XY = sorted([list(map(int, input().split())) for _ in range(n)])

    if n == 1:
        print(1)
        exit()

    res = n
    for i in range(n):
        x1, y1 = XY[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = XY[j]
            # ベクトル(dx, dy)を決める
            dx, dy = x2 - x1, y2 - y1

            cnt = 0
            # 二点間のベクトルが(dx, dy)に一致すればその分コストが0になる
            for k in range(n):
                x3, y3 = XY[k]
                for l in range(n):
                    if k == l:
                        continue
                    x4, y4 = XY[l]
                    if dx == x4 - x3 and dy == y4 - y3:
                        cnt += 1

            res = min(res, n - cnt)

    print(res)


if __name__ == '__main__':
    resolve()
