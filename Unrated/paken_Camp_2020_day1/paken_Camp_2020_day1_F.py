# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19532128
# F - Fibonaccyan
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    p = int(input())
    if p == 1:
        print(1)
        exit()

    MAX = 10 ** 6
    fib = [1] * MAX
    for i in range(2, MAX):
        fib[i] = (fib[i - 2] + fib[i - 1]) % p
        if fib[i] == 0:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
