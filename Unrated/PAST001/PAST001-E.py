# https://atcoder.jp/contests/past201912-open/tasks/past201912_e
# E - SNS のログ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(q)]
    res = list(["N"] * n for _ in range(n))

    # 操作をそのまま実装する
    # 自分自身をフォロー(a = b)してしまわないように注意
    for i in s:
        if i[0] == 1:
            a, b = i[1] - 1, i[2] - 1
            res[a][b] = "Y"
        elif i[0] == 2:
            a = i[1] - 1
            for b in range(n):
                if b != a and res[b][a] == "Y":
                    res[a][b] = "Y"
        else:
            a = i[1] - 1
            f = []
            for x in range(n):
                if x != a and res[a][x] == "Y":
                    f.append(x)
            for x in f:
                for b in range(n):
                    if b != a and res[x][b] == "Y":
                        res[a][b] = "Y"

    for i in range(n):
        print("".join(res[i]))


if __name__ == '__main__':
    resolve()
