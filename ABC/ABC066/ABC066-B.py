# https://atcoder.jp/contests/abc066/submissions/12860316
# B - ss
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input())
    S.pop()
    while len(S) != 1:
        n = len(S)
        if n % 2 == 0:
            if S[: n // 2] == S[n // 2:]:
                break
        S.pop()

    print(len(S))


if __name__ == '__main__':
    resolve()
