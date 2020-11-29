# https://atcoder.jp/contests/arc109/submissions/18489958
# C - Large RPS Tournament
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def check(a, b):
        if a == "R" and b == "R":
            return a
        elif a == "R" and b == "P":
            return b
        elif a == "R" and b == "S":
            return a
        elif a == "P" and b == "R":
            return a
        elif a == "P" and b == "P":
            return a
        elif a == "P" and b == "S":
            return b
        elif a == "S" and b == "R":
            return b
        elif a == "S" and b == "P":
            return a
        elif a == "S" and b == "S":
            return a

    def dfs(K, offset):
        if K == 0:
            return S[offset]
        if memo[K][offset] != "?":
            return memo[K][offset]
        offset2 = (offset + two[K - 1]) % n
        zenhan = dfs(K - 1, offset)
        kouhan = dfs(K - 1, offset2)
        memo[K][offset] = check(zenhan, kouhan)
        return memo[K][offset]

    n, k = map(int, input().split())
    S = input()

    two = [1] * (k + 1)
    for i in range(k):
        two[i + 1] = two[i] * 2 % n

    memo = [["?"] * (n + 1) for _ in range(k + 1)]
    res = dfs(k, 0)
    print(res)


if __name__ == '__main__':
    resolve()
