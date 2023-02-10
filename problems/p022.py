'''
https://projecteuler.net/problem=22
Names scores
'''


def main() -> int:
    '''Returns the numerical value * position of a alphabetically sorted list of names.'''
    names = process_data()
    numerical_values = map(numerical_value_of_name, names)

    result = sum((k+1)*nv for k, nv in enumerate(numerical_values))
    return result


def numerical_value_of_name(name: str) -> int:
    '''Returns the numerical value of a word by using the build in ord function. 
    This works for upper case words.'''
    NORMALIZER = ord('A')-1

    result = sum((ord(letter.upper())-NORMALIZER) for letter in name)
    return result


def process_data():
    '''Formats the names.txt into an array of names that is sorted alphabetically. 
    First and last entry have an extra " and we must cut it off.'''
    DIR = 'data/' + 'p022_names.txt'
    
    with open(DIR, 'r') as NAMES:
        NAMES_ARR = NAMES.read().split('","')
        NAMES_ARR[0], NAMES_ARR[-1] = NAMES_ARR[0][1:], NAMES_ARR[-1][:-1]

    result = sorted(NAMES_ARR)
    return result


if __name__ == '__main__':
    result = main()
    print(result)
