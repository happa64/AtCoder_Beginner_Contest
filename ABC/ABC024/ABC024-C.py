# https://atcoder.jp/contests/abc024/submissions/13170697
# C - 民族大移動
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d, k = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(d)]
    ST = [list(map(int, input().split())) for _ in range(k)]

    for s, t in ST:
        for i in range(d):
            l, r = LR[i]
            if s <= t:
                if l <= s <= r and l <= t <= r:
                    print(i + 1)
                    break
                else:
                    if l <= s <= r:
                        s = r
            else:
                if l <= s <= r and l <= t <= r:
                    print(i + 1)
                    break
                else:
                    if l <= s <= r:
                        s = l


if __name__ == '__main__':
    resolve()
