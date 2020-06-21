# https://atcoder.jp/contests/arc020/submissions/14512223
# A - 石を滑らせるゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print("Ant" if abs(a) < abs(b) else "Bug" if abs(a) > abs(b) else "Draw")


if __name__ == '__main__':
    resolve()
