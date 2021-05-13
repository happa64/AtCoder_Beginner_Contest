# https://codeforces.com/contest/1511/submission/116013296
# C - Yet Another Card Deck


def solve():
    n, q = map(int, input().split())
    A = tuple(map(int, input().split()))
    T = tuple(map(int, input().split()))

    used_col = set()
    B = []
    for i, a in enumerate(A):
        if a in used_col:
            continue
        used_col.add(a)
        B.append([a, i + 1])

    m = len(B)
    res = [0] * q
    for i, t in enumerate(T):
        for j in range(m):
            if B[j][0] == t:
                ind = B[j][1]
                res[i] = ind
                B[j][1] = 1
                for k in range(m):
                    if j == k:
                        continue
                    if B[k][1] < ind:
                        B[k][1] += 1
                break
    print(*res)


if __name__ == '__main__':
    solve()
