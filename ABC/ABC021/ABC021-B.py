# https://atcoder.jp/contests/abc021/submissions/13970526
# B - 嘘つきの高橋くん
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a, b = map(int, input().split())
    k = int(input())
    P = [a] + list(map(int, input().split())) + [b]

    print("YES" if len(P) == len(set(P)) else "NO")


if __name__ == '__main__':
    resolve()
