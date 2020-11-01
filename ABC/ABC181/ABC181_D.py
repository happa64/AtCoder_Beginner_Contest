# https://atcoder.jp/contests/abc181/submissions/17799290
# D - Hachi
import sys
from collections import Counter
from itertools import permutations
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    D_init = Counter(S)

    if len(S) < 3:
        for pattern in permutations(S):
            p = int("".join(pattern))
            if p % 8 == 0:
                print("Yes")
                break
        else:
            print("No")
    else:
        for i in range(100, 1000):
            if i % 2 == 0:
                j = (i // 2) % 100
                if j % 4 == 0:
                    T = str(i)
                    D = deepcopy(D_init)
                    for t in T:
                        if D[t]:
                            D[t] -= 1
                        else:
                            break
                    else:
                        print("Yes")
                        break
        else:
            print("No")


if __name__ == '__main__':
    resolve()
