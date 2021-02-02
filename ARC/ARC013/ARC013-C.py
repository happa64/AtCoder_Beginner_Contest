# https://atcoder.jp/contests/arc013/submissions/19882163
# C - 笑いをとれるかな？
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())
    cut = []
    for _ in range(N):
        X, Y, Z = map(int, input().split())
        M = int(input())
        x_list, y_list, z_list = [], [], []
        for _ in range(M):
            x, y, z = map(lambda w: int(w) + 1, input().split())
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
        min_x, max_x = min(x_list), max(x_list)
        min_y, max_y = min(y_list), max(y_list)
        min_z, max_z = min(z_list), max(z_list)
        cut.append(min_x - 1)
        cut.append(X - max_x)
        cut.append(min_y - 1)
        cut.append(Y - max_y)
        cut.append(min_z - 1)
        cut.append(Z - max_z)
    res = list(accumulate(cut, lambda a, b: a ^ b))[-1]
    print("WIN" if res else "LOSE")


if __name__ == '__main__':
    resolve()
