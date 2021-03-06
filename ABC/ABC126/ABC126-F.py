# https://atcoder.jp/contests/abc126/submissions/17191878
# F - XOR Matching
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def debug(L, k):
    n = len(L)
    used = set()
    for i in range(n):
        if L[i] in used:
            continue
        used.add(L[i])
        t = L[i]
        for j in range(i + 1, n):
            t ^= L[j]
            if L[i] == L[j]:
                break
        if t != k:
            return False
    return True


def resolve():
    m, k = map(int, input().split())

    MAX = pow(2, m)
    if MAX <= k or (m == 1 and k == 1):
        print(-1)
        exit()

    if m == 1 and k == 0:
        print("0 0 1 1")
        exit()

    res = []
    for i in range(MAX):
        if i == k:
            continue
        res.append(i)
    res.append(k)
    for i in reversed(range(MAX)):
        if i == k:
            continue
        res.append(i)
    res.append(k)
    print(*res)
    # print(debug(res, k))


if __name__ == '__main__':
    resolve()
