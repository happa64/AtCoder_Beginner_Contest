# https://atcoder.jp/contests/code-thanks-festival-2018-open/submissions/15758349
# B - Colored Balls
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    if (x + y) % 4 != 0:
        print("No")
    else:
        if (3 * x - y) % 8 == 0:
            b = (3 * x - y) // 8
            a = x - 3 * b
            if a >= 0 and b >= 0:
                if a + 3 * b == x and 3 * a + b == y:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")


if __name__ == '__main__':
    resolve()
