# https://atcoder.jp/contests/arc001/submissions/14445822
# A - センター採点
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = input()

    res_min = f_inf
    res_max = 0
    for i in range(1, 5):
        score = 0
        for c in C:
            if i == int(c):
                score += 1
        res_min = min(res_min, score)
        res_max = max(res_max, score)

    print(res_max, res_min)


if __name__ == '__main__':
    resolve()
