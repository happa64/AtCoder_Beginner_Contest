# https://atcoder.jp/contests/agc009/tasks/agc009_a
# A - Multiple Array
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)][::-1]

    # 後ろからBの倍数になるように押していく
    res = 0
    for i in range(n):
        a, b = AB[i]
        push = ((a + res + b - 1) // b) * b - a
        res = push

    print(res)


if __name__ == '__main__':
    resolve()
