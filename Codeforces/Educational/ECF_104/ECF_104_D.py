# https://codeforces.com/contest/1487/submission/109072567
# D - Pythagorean Triples


def solve():
    n = int(input())
    res = 0
    for a in range(2, 10 ** 9):
        a2 = pow(a, 2)
        if a2 <= 2 * n + 1:
            if (a2 - 1) % 2 == 0:
                b = (a2 - 1) // 2
                if a <= b <= n:
                    c = a2 - b
                    if b <= c <= n:
                        res += 1
        else:
            break
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
