import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    res = 0
    for i in range(n):

        # A[i]の転倒数を求める
        x = 0
        for j in range(i + 1, n):
            if A[i] > A[j]:
                x += 1

        # A[i]より小さい数を求める
        y = 0
        for j in range(n):
            if A[i] > A[j]:
                y += 1

        res += x * k
        res %= mod
        res += y * (k - 1) * k // 2
        res %= mod

    print(res)


if __name__ == '__main__':
    resolve()
