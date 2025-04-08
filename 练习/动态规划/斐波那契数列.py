import math


def fib_formula(self, n: int) -> int:
    # 时间复杂度：O(log n)
    # 空间复杂度：O(1)
    # 解析：斐波那契数列公式
    return (
        1
        / math.sqrt(5)
        * (pow((1 + math.sqrt(5)) / 2, n + 1) - pow((1 - math.sqrt(5)) / 2, n + 1))
    )


def fib(self, n: int) -> int:
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    # 解析：斐波那契数列
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def fib_matrix(self, n: int) -> int:
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
        return 0
    else:
        M = [1, 1, 1, 0]
        return matrix_pow(M, n - 1)[0]
