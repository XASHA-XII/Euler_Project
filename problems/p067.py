import numpy as np


from p018 import max_path_in_lattice


def main() -> int:
    DIR = 'data/' + 'p067_triangle.txt'

    lattice = process_data(DIR)

    result = max_path_in_lattice(lattice)

    return result


def process_data(path: str) -> np.ndarray:
    '''Format triangle.txt into a lower triangular matrix.'''
    with open(path, 'r') as TRIANGLE:
        lattice = [list(map(lambda x: int(x), row.split()))
                   for row in TRIANGLE.read().split("\n")]
        lattice.pop()  # the last row is empty
        n = len(lattice)

        result = np.zeros((n, n), dtype=np.int64)
        for k, row in enumerate(lattice):
            result[k, :k+1] = row

        return result


if __name__ == '__main__':
    result = main()
    print(result)
