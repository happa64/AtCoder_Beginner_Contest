# https://atcoder.jp/contests/abc187/submissions/19117411
# A - Large Digits
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


# nの桁和を返す
def digit_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def resolve():
    a, b = map(int, input().split())

    A = digit_sum(a)
    B = digit_sum(b)
    print(max(A, B))


if __name__ == '__main__':
    resolve()
