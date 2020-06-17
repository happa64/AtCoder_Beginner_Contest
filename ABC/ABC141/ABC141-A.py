# https://atcoder.jp/contests/abc141/submissions/13665495
# A - Weather Prediction
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input().rstrip()
    print("Cloudy" if s == "Sunny" else "Sunny" if s == "Rainy" else "Rainy")


if __name__ == '__main__':
    resolve()
