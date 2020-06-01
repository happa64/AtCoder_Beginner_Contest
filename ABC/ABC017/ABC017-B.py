# https://atcoder.jp/contests/abc017/submissions/13939168
# B - choku語
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = input()

    pos = 0
    while pos < len(x):
        if x[pos:pos + 2] == "ch":
            pos += 2
        elif x[pos] == "o":
            pos += 1
        elif x[pos] == "k":
            pos += 1
        elif x[pos] == "u":
            pos += 1
        else:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()
