# https://atcoder.jp/contests/past202005/submissions/14065689
# I - 行列操作
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def response(x, y):
        print(n * (x - 1) + y - 1)

    n = int(input())
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    row = list(range(1, n + 1))
    colum = list(range(1, n + 1))
    flg = 1
    for i in range(q):
        if query[i][0] == 1:
            _, a, b = query[i]
            if flg:
                row[a - 1], row[b - 1] = row[b - 1], row[a - 1]
            else:
                colum[a - 1], colum[b - 1] = colum[b - 1], colum[a - 1]
        elif query[i][0] == 2:
            _, a, b = query[i]
            if flg:
                colum[a - 1], colum[b - 1] = colum[b - 1], colum[a - 1]
            else:
                row[a - 1], row[b - 1] = row[b - 1], row[a - 1]
        elif query[i][0] == 3:
            flg ^= 1
        else:
            _, a, b = query[i]
            response(row[a - 1], colum[b - 1]) if flg else response(row[b - 1], colum[a - 1])


if __name__ == '__main__':
    resolve()
