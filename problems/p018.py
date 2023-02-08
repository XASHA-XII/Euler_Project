import numpy as np


def main() -> int:
    lattice = process_data(TRIANGLE)
    result = max_path_in_lattice(lattice)
    return result


def max_path_in_lattice(lattice: np.ndarray) -> int:
    '''Returns the maximal path in a binomial lattice of length >=1. 
    To take advantage of vectorization, we use numpy for this problem.'''
    N = len(lattice)
    for k in reversed(range(1, N)):
        lattice[k-1, :k] += np.maximum(lattice[k, :k], lattice[k, 1:k+1])
    return lattice[0, 0]


def process_data(triangle: str) -> np.ndarray:
    '''Format a triangular string into a lower triangular matrix.'''
    lattice = [list(map(lambda x: int(x), row.split()))
               for row in TRIANGLE.split("\n")]
    n = len(lattice)

    result = np.zeros((n, n), dtype=np.int64)
    for k, row in enumerate(lattice):
        result[k, :k+1] = row
    return result


TRIANGLE = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


if __name__ == '__main__':
    result = main()
    print(result)
