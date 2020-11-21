# https://atcoder.jp/contests/arc108/submissions/18257248
# A - Sum and Product
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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
    s, p = map(int, input().split())

    div = make_divisors(p)
    for n in div:
        m = p // n
        if n + m == s:
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    resolve()
