class BinarySearch:
    def meguru_bisect(self, is_ok, left, right):
        """
        :param is_ok: 定義して下さい
        :param left: 取りうる最小の値-1
        :param right: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(left - right) > 1:
            mid = (left + right) // 2
            if is_ok(mid):
                left = mid
            else:
                right = mid
        return left

