# https://atcoder.jp/contests/arc007/submissions/14168065
# B - 迷子のCDケース
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    disk = list(int(input()) for _ in range(m))
    case = list(range(n + 1))

    for num in disk:
        idx = case.index(num)
        case[0], case[idx] = case[idx], case[0]

    print(*case[1:], sep="\n")


if __name__ == '__main__':
    resolve()
