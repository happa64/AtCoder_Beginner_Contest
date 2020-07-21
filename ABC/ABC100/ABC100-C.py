# https://atcoder.jp/contests/abc100/submissions/13574627
# C - *3 or /2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    even = [A[i] for i in range(n) if A[i] % 2 == 0]

    res = 0
    for number in even:
        while number % 2 == 0:
            res += 1
            number //= 2

    print(res)


if __name__ == '__main__':
    resolve()
