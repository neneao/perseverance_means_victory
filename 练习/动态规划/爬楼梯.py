def climbStairs_DP1(self, n: int) -> int:
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    # 解析：动态规划
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        # 解析：f(i) = f(i-1) + f(i-2)
        # # 解释：f(i)表示到达第i级台阶的方法数
        # # 解释：到达第i级台阶的方法数可以分为两种情况：
        # # 1. 从第i-1级台阶上来（即上一步只走了一步）
        # # 2. 从第i-2级台阶上来（即上一步走了两步）
        # # 解释：所以到达第i级台阶的方法数等于到达第i-1级台阶的方法数加上到达第i-2级台阶的方法数
        # # 解释：即f(i) = f(i-1) + f(i-2)
    return dp[n]


def climbStairs_DP2(self, n: int) -> int:
    n1, n2 = 1, 1
    for _ in range(n - 1):
        n1, n2 = n2, n1 + n2
    return n2


def climbStairs(self, n: int) -> int:
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    # 解析：
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        c = [1, 2, 3]
        for i in range(2, n):
            c[i % 3] = sum(c) - c[i % 3]
        return c[i % 3]


import math


def climbStairs_Fib(self, n: int) -> int:
    # 时间复杂度：O(log n)
    # 空间复杂度：O(1)
    # 解析：斐波那契数列公式
    return (
        1
        / math.sqrt(5)
        * (pow((1 + math.sqrt(5)) / 2, n + 1) - pow((1 - math.sqrt(5)) / 2, n + 1))
    )


def climbStairs_Matrix(self, n: int) -> int:
    # 时间复杂度：O(log n)
    # 空间复杂度：O(1)
    # 解析：矩阵快速幂
    def matrix_mult(A, B):
        return [
            A[0] * B[0] + A[1] * B[2],
            A[0] * B[1] + A[1] * B[3],
            A[2] * B[0] + A[3] * B[2],
            A[2] * B[1] + A[3] * B[3],
        ]

    def matrix_pow(A, n):
        if n == 1:
            return A
        elif n % 2 == 0:
            half = matrix_pow(A, n // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(A, matrix_pow(A, n - 1))

    if n <= 2:
        return n
    F = [1, 1, 1, 0]
    result = matrix_pow(F, n - 1)
    return result[0]
