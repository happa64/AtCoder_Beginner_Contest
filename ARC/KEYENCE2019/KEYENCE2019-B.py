# https://atcoder.jp/contests/keyence2019/submissions/12537533
# B - KEYENCE String
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())
    n = len(s)

    if "".join(s) == "keyence":
        print("YES")
        exit()

    for i in range(n):
        ss = s[::]
        for j in range(i, n):
            ss.pop(i)
            if "".join(ss) == "keyence":
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")


if __name__ == '__main__':
    resolve()
