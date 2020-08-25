# https://atcoder.jp/contests/joi2019yo/submissions/16225546
# A - ソーシャルゲーム (Social Game)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    max_day = (c + a - 1) // a
    score = 0
    for i in range(1, max_day + 2):
        score += a
        if i % 7 == 0:
            score += b
        if score >= c:
            print(i)
            break


if __name__ == '__main__':
    resolve()
