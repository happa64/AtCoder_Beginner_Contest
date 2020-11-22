# https://atcoder.jp/contests/abc184/submissions/18308535
# B - Quizzes
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    S = input()

    for s in S:
        if s == "o":
            x += 1
        else:
            x -= 1
        x = max(0, x)
    print(x)


if __name__ == '__main__':
    resolve()
