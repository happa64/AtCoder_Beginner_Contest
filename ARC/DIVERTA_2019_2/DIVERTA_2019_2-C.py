# https://atcoder.jp/contests/diverta2019-2/submissions/14417576
# C - Successive Subtraction
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    if len(A) == 2 and 0 in A:
        print(max(A) - 0)
        print(max(A), 0)
        exit()

    plus = deque(sorted([a for a in A if a >= 0]))
    minus = deque(sorted([a for a in A if a < 0]))

    res = []
    if plus and minus:
        while len(plus) > 1:
            x = minus.pop()
            y = plus.pop()
            res.append([x, y])
            minus.append(x - y)
        while minus:
            x = plus.pop()
            y = minus.pop()
            res.append([x, y])
            plus.append(x - y)
    elif plus:
        x = plus.popleft()
        y = plus.pop()
        res.append([x, y])
        minus.append(x - y)
        while len(plus) > 1:
            x = minus.pop()
            y = plus.pop()
            res.append([x, y])
            minus.append(x - y)
        x = plus.pop()
        y = minus.pop()
        res.append([x, y])
        plus.append(x - y)
    else:
        x = minus.pop()
        y = minus.popleft()
        res.append([x, y])
        plus.append(x - y)
        while minus:
            x = plus.pop()
            y = minus.pop()
            res.append([x, y])
            plus.append(x - y)

    print(*plus)
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
