class Gcd:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def ngcd(self, A):
        res = A[0]
        for i in range(len(A)):
            if res != 1:
                res = gcd(A[i], res)
        return res

    def lcm(self, a, b):
        return a * b // gcd(a, b)

    def nlcm(self, A):
        res = A[0]
        for i in range(len(A)):
            res = lcm(res, A[i])
        return res
