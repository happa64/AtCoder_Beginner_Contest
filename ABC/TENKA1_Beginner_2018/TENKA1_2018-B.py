# https://atcoder.jp/contests/tenka1-2018-beginner/submissions/13630774
# B - Exchange
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, k = map(int, input().split())

    for i in range(k):
        if i % 2 == 0:
            if a % 2:
                a -= 1
                b += a // 2
                a //= 2
            else:
                b += a // 2
                a //= 2
        else:
            if b % 2:
                b -= 1
                a += b // 2
                b //= 2
            else:
                a += b // 2
                b //= 2

    print(a, b)


if __name__ == '__main__':
    resolve()
