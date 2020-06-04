# https://atcoder.jp/contests/abc025/submissions/13993326
# B - 双子とスイカ割り
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())

    res = 0
    for i in range(n):
        s, d = input().split()
        d = int(d)
        if s == "East":
            res += a if d < a else d if a <= d <= b else b
        else:
            res -= a if d < a else d if a <= d <= b else b

    print("West", abs(res)) if res < 0 else print("East", res) if res > 0 else print(0)


if __name__ == '__main__':
    resolve()
