def divisible_by_3_and_5(n: int) -> int:
    '''Sum of all positive integers smaller than some number'''
    result = sum(k for k in range(n) if (k % 3) == 0 or (k % 5) == 0)
    return result


def main() -> None:
    N = 1000
    result = divisible_by_3_and_5(N)
    print(result)


if __name__ == '__main__':
    main()
