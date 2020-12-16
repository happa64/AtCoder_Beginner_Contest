import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for j in range(n):
            if i - A[j] >= 0 and dp[i - A[j]] == 0:
                dp[i] = 1
    print("First" if dp[-1] else "Second")


if __name__ == '__main__':
    resolve()
