# https://atcoder.jp/contests/zone2021/submissions/22229620
# B - 友好の印
import sys

sys.setrecursionlimit(10 ** 7)
if sys.platform == 'ios':
    sys.stdin = open('input_file.txt')
else:
    input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, D, H = map(int, input().split())
    DH = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for d, h in DH:
        a = max(0, h - (H - h) / (D - d) * d)
        res = max(res, a)
    print(res)


if __name__ == '__main__':
    solve()