# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432cc7/0000000000433157
# Crazy Rows
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for idx in range(t):
        n = int(input())
        grid = [input().rstrip() for _ in range(n)]

        right = [0] * n
        for i in range(n):
            r = -1
            for j in reversed(range(n)):
                if grid[i][j] == "1":
                    r = j
                    break
            right[i] = r + 1

        res = 0
        for i in range(n):
            if right[i] <= i + 1:
                continue
            for j in range(i + 1, n):
                if right[j] <= i + 1:
                    res += j - i
                    t = right.pop(j)
                    right.insert(i, t)
                    break
        print("Case #{}: {}".format(idx + 1, res))


if __name__ == '__main__':
    resolve()
