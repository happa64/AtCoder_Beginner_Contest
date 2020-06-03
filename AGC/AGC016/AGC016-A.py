import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    D = Counter(s)
    print(len(s), D)


if __name__ == '__main__':
    resolve()
