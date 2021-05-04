import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b, c = map(int, input().split())
    print("Yes" if a ** 2 + b ** 2 < c ** 2 else "No")


if __name__ == '__main__':
    solve()
