# https://atcoder.jp/contests/arc022/submissions/14512353
# A - スーパーICT高校生
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())

    res = []
    while s:
        a = s.pop(0)
        if len(res) == 0 and a.upper() == "I":
            res.append(a)
        elif len(res) == 1 and a.upper() == "C":
            res.append(a)
        elif len(res) == 2 and a.upper() == "T":
            res.append(a)
    print("YES" if len(res) == 3 else "NO")


if __name__ == '__main__':
    resolve()
