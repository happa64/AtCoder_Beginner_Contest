# https://atcoder.jp/contests/diverta2019/submissions/12841343
# D - DivRem Number
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


# 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def resolve():
    n = int(input())

    # n = k(m + 1)より、nの約数から1引いた数が、お気に入りの整数の候補となる
    # 約数を列挙し、約数-1が条件にあうか確かめる
    div = make_divisors(n)
    res = 0
    for i in div:
        if i != 1:
            x, y = divmod(n, i - 1)
            if x == y:
                res += i - 1

    print(res)


if __name__ == '__main__':
    resolve()
