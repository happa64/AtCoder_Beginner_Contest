# https://atcoder.jp/contests/arc006/submissions/13591470
# B - あみだくじ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, l = map(int, input().split())
    amida = [list(input()) for _ in range(l)]
    goal = list(input())

    for first in range(0, 2 * n - 1, 2):
        pos = first
        depth = 0
        while depth < l:
            if amida[depth][max(0, pos - 1)] == "-":
                pos -= 2
            elif amida[depth][min(2 * n - 2, pos + 1)] == "-":
                pos += 2
            depth += 1

        if goal[pos] == "o":
            print(first // 2 + 1)
            break


if __name__ == '__main__':
    resolve()
