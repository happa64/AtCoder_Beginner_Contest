# https://atcoder.jp/contests/abc142/tasks/abc142_c
# C - Go to School
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    B = []
    # 生徒iが登校した時点で教室に居た人数という配列を作り、教室に居た人数順に昇順ソートする
    for i in range(n):
        B.append([i + 1, A[i]])
    B = sorted(B, key=lambda x: x[1])

    res = []
    for i in range(n):
        res.append(B[i][0])

    print(*res)


if __name__ == '__main__':
    resolve()
