# https://atcoder.jp/contests/arc116/submissions/21425749
# A - Odd vs Even
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())

    even = 0
    while n % 2 == 0:
        n //= 2
        even += 1

    if even == 0:
        print("Odd")
    elif even == 1:
        print("Same")
    else:
        print("Even")


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()
