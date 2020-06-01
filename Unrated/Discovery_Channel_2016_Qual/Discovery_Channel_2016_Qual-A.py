# https://atcoder.jp/contests/discovery2016-qual/submissions/13908449
# A - DISCO presents ディスカバリーチャンネルプログラミングコンテスト 2016
import sys
import math
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    w = int(input())
    S = "DiscoPresentsDiscoveryChannelProgrammingContest2016"

    start, end = 0, w
    for i in range(math.ceil(len(S) / w)):
        print(S[start:end])
        start += w
        end += w


if __name__ == '__main__':
    resolve()
