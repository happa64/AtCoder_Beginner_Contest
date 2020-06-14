import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    for x in range(k if k < 50 else 50):
        B = [0] * n
        for j in range(n):
            l = max(0, j - A[j])
            r = min(n - 1, j + A[j])
            B[l] += 1
            if r + 1 < n:
                B[r + 1] -= 1

        for x in range(1, n):
            B[x] += B[x - 1]
        A = B

    print(*A)


if __name__ == '__main__':
    resolve()
