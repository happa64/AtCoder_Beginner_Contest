# https://atcoder.jp/contests/agc019/tasks/agc019_a
# A - Ice Tea Store
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    q, h, s, d = map(int, input().split())
    n = int(input())
    t = min(q * 4, h * 2, s)

    if n == 1:
        print(int(t))
    else:
        if n % 2 == 0:
            print(int(min(t * n, d * n // 2)))
        else:
            # オーバーフローに注意
            print(int(min(t * n, d * ((n - 1) // 2) + t)))


if __name__ == '__main__':
    resolve()
