# https://atcoder.jp/contests/typical90/submissions/24158053
# 085 - Multiplication 085（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def solve():
    k = int(input())
    div = make_divisors(k)
    n = len(div)
    res = 0
    for i in range(n):
        a = div[i]
        for j in range(i, n):
            b = div[j]
            if k % (a * b) == 0:
                c = k // (a * b)
                if b <= c:
                    res += 1
    print(res)


if __name__ == '__main__':
    solve()
