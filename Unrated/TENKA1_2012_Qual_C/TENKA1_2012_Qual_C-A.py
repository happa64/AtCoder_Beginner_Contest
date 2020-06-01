# https://atcoder.jp/contests/tenka1-2012-qualC/submissions/13909069
# A - 与えられた数より小さい素数の個数について
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(pow(n, 0.5)) + 1):
        if n % k == 0:
            return False
    return True


def resolve():
    n = int(input())

    res = 0
    for i in range(1, n):
        res += 1 if is_prime(i) else 0

    print(res)


if __name__ == '__main__':
    resolve()
