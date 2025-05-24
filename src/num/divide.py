def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) != (divisor < 0)

    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    for i in range(31, -1, -1):
        temp_divident = dividend >> i
        if temp_divident >= divisor:
            quotient += 1 << i
            t = divisor << i
            dividend -= t

    return -quotient if negative else quotient


a = divide(15, 3)
print(a)