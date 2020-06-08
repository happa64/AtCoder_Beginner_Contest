# https://atcoder.jp/contests/abc023/submissions/14105104
# A - 加算王
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
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
    x = int(input())
    print(digit_sum(x))


if __name__ == '__main__':
    resolve()
