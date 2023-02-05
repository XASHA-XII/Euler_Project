import math
import functools


def main() -> None:
    N = 20
    result = functools.reduce(math.lcm, range(1, N+1))
    print(result)


if __name__ == '__main__':
    main()
