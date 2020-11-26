# https://atcoder.jp/contests/abc161/submissions/18413072
# E - Yutori
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k, c = map(int, input().split())
    S = input()

    used_front = set()
    cnt = 0
    for i in range(n):
        if cnt:
            cnt -= 1
        else:
            if S[i] == "o":
                used_front.add(i + 1)
                cnt = c

    if len(used_front) > k:
        print("")
        exit()

    used_back = set()
    cnt = 0
    for i in reversed(range(n)):
        if cnt:
            cnt -= 1
        else:
            if S[i] == "o":
                used_back.add(i + 1)
                cnt = c

    res = list(used_front & used_back)
    res.sort()
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
