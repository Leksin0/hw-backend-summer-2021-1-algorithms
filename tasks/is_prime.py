import math
__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
