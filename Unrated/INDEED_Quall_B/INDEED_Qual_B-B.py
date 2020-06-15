# https://atcoder.jp/contests/indeednow-qualb/submissions/14386321
# B - 高橋くんと文字列操作
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = deque(list(input()))
    t = list(input())

    for i in range(1000):
        if list(s) == t:
            print(i)
            break
        a = s.pop()
        s.appendleft(a)
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
