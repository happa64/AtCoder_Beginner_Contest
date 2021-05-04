import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    a = max(A)
    b = min(B)
    res = max(0, b - a + 1)
    print(res)


if __name__ == '__main__':
    solve()
