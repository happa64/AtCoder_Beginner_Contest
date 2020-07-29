# https://atcoder.jp/contests/arc093/submissions/15521557
# D - Grid Components
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    res = [[""] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            res[i][j] = "." if i < 50 else "#"

    b -= 1
    for i in range(0, 50, 2):
        for j in range(0, 100, 2):
            if b == 0:
                break
            res[i][j] = "#"
            b -= 1
        else:
            continue
        break

    a -= 1
    for i in reversed(range(50, 100, 2)):
        for j in range(0, 100, 2):
            if a == 0:
                break
            res[i][j] = "."
            a -= 1
        else:
            continue
        break

    print(100, 100)
    for i in res:
        print("".join(i))


if __name__ == '__main__':
    resolve()
