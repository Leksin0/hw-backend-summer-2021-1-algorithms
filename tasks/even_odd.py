__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    even = sum(i for i in numbers if abs(i) % 2 == 0)
    odd = sum(i for i in numbers if abs(i) % 2 != 0)
    if odd == 0:
        return 0
    return even/odd
