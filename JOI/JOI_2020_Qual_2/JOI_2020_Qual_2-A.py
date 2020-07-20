# https://atcoder.jp/contests/joi2020yo1b/submissions/15326086
# A - 試験 (Exam)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = sorted(list(map(int, input().split())))
    res = sum(ABC[1:])
    print(res)


if __name__ == '__main__':
    resolve()
