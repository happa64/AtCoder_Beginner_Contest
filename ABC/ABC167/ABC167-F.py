# https://atcoder.jp/contests/abc167/submissions/20630279
# F - Bracket Sequencing
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())

    L = R = 0
    LR = []
    for _ in range(n):
        S = input().rstrip()
        l = r = 0
        for s in S:
            if s == "(":
                l += 1
            else:
                if l:
                    l -= 1
                else:
                    r += 1
        if l and not r:
            L += l
        elif not l and r:
            R += r
        elif l and r:
            LR.append([r - l, l])

    LR.sort(key=lambda x: [-x[0], x[1]])
    for lr, l in LR:
        if R < l:
            print("No")
            break
        else:
            R += lr
    else:
        print("Yes" if R == L else "No")


if __name__ == '__main__':
    solve()
