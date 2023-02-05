import os
import itertools

from p006 import sum_formula


def order_of_string(string: str) -> int:
    ''' Returns the numerical order of a upper case string. For example "BABY" is 2+1+2+25=30'''
    result = sum(ord(char) - ord('A') + 1 for char in string)
    return result


def neccesary_triangles(n: int) -> list[int]:
    '''Returns a list of all triangle numbers smaller or equal to n>=3'''
    triangle_numbers = []
    for k in itertools.count(1):
        triangle_number = sum_formula(k)
        if triangle_number > n:
            break
        else:
            triangle_numbers.append(triangle_number)
    return triangle_numbers


def main():
    ''' Returns the number of triangle word in the file p042_words.txt. 
    Triangle words are words whose numerical value corresponds to a number of the form n*(n+1)/2.
    To this end, we convert the txt-file to a list of their corresponding numerical values.
    Then we compute all triangle numbers up to the maximum of list of numerical values.'''

    file_path = os.path.join(os.getcwd(), 'data', 'p042_words.txt')

    with open(file_path, 'r') as LIST_OF_WORDS:
        numerical_words = [order_of_string(
            word.strip('"')) for word in LIST_OF_WORDS.read().split(',')]

    max_value = max(numerical for numerical in numerical_words)
    necc_triangles = neccesary_triangles(max_value)

    result = sum(
        1 for numerical in numerical_words if numerical in necc_triangles)
    print(result)


if __name__ == '__main__':
    main()
