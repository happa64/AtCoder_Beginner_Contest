# https://atcoder.jp/contests/joi2014yo/submissions/15124200
# A - 平均点 (Average Score)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    score = list(int(input()) for _ in range(5))
    res = 0
    for i in score:
        res += 40 if i < 40 else i
    print(res // 5)


if __name__ == '__main__':
    resolve()
