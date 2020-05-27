import sys
import bisect

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    T = input()

    for t in T:
        if t not in set(S):
            print(-1)
            exit()

    D = {}
    for i in range(len(S)):
        if D.get(S[i]) is None:
            D[S[i]] = i
        else:
            t = ([D.get(S[i])] if type(D.get(S[i])) == int else D.get(S[i])) + [i]
            D[S[i]] = t

    cnt = 1
    pre = min(D[T[0]]) if type(D[T[0]]) == list else D[T[0]]
    i = 1
    while i < len(T):
        if type(D[T[i]]) == list:
            for j in D[T[i]]:
                if pre < j:
                    idx = j
                    break
            else:
                cnt += 1
        else:
            idx = D[T[i]]
            if idx < pre:
                cnt += 1

        pre = idx
        i += 1

    print(pre)
    res = len(S) * cnt - (len(S) - 1 - pre)
    print(res)


if __name__ == '__main__':
    resolve()
