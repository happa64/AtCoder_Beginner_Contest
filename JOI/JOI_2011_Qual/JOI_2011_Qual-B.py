# https://atcoder.jp/contests/joi2011yo/submissions/15050196
# B - 指輪 (Ring)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    target = input()
    n = int(input())
    res = 0
    for _ in range(n):
        s = input() * 2
        for i in range(20):
            ss = s[i: i + len(target)]
            if ss == target:
                res += 1
                break
    print(res)


if __name__ == '__main__':
    resolve()
