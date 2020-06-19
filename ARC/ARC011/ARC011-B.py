# https://atcoder.jp/contests/arc011/submissions/13152323
# B - ルイス・キャロルの記憶術
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    W = list(map(str, input().split()))

    dict = {"b": 1, "c": 1, "d": 2, "w": 2, "t": 3, "j": 3, "f": 4, "q": 4, "l": 5, "v": 5, \
            "s": 6, "x": 6, "p": 7, "m": 7, "h": 8, "k": 8, "n": 9, "g": 9, "z": 0, "r": 0}

    res = []
    for w in W:
        num = ""
        for s in w:
            if dict.get(s.lower()) is not None:
                num += str(dict[s.lower()])
        if num != "":
            res.append(num)

    print(*res)


if __name__ == '__main__':
    resolve()
