from module_a import get_divisor


def compute_ratio(y: int) -> float:
    divisor = get_divisor(y)
# 当 divisor == 0 时，会触发 ZeroDivisionError
    return 10 / divisor


if __name__ == "__main__":

   print(compute_ratio(0))
