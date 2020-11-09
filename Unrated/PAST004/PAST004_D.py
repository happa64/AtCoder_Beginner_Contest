# https://atcoder.jp/contests/past202010-open/submissions/18010696
# D - 分身
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S_init = input()

    res = f_inf
    for x in range(n + 1):
        for y in range(n + 1):
            S = list(S_init)
            for i in range(n):
                if S[i] == "#":
                    for j in range(x):
                        if i - (j + 1) >= 0:
                            S[i - (j + 1)] = "#"

            for i in reversed(range(n)):
                if S[i] == "#":
                    for j in range(y):
                        if i + (j + 1) < n:
                            S[i + (j + 1)] = "#"

            if S.count("#") == n:
                if res > x + y:
                    res = min(res, x + y)
                    ans = [x, y]

    print(*ans)


if __name__ == '__main__':
    resolve()
