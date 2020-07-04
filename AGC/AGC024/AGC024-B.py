import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(int(input()) for _ in range(n))

    res = [0] * (n + 1)
    for p in P:
        res[p] = res[p - 1] + 1
    print(n - max(res))


if __name__ == '__main__':
    resolve()
