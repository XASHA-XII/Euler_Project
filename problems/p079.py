from typing import List, Dict, Set

''''
https://projecteuler.net/problem=79
Passcode derivation
'''


def main() -> int:
    """Returns the shortest password that can be derived from the keylogs.

    Returns:
        int: The password
    """
    DIR = 'data/' + 'p079_keylog.txt'
    keylogs = process_data(DIR)
    ordered_password_keys = process_keylogs(keylogs)
    result = get_pass(ordered_password_keys)
    return result


def process_keylogs(keylogs: List[str]) -> Dict[str, Set[str]]:
    """Returns a dicionary of all the digits in the keylog and the set of numbers that appear after them in any keylog. For example for 312
    in keylogs we get {3:{12}, 1:{2}, 2:{}}.

    Args:
        keylogs (List[str]): The keylogs

    Returns:
        Dict[str, Set[str]]: The dicionary of the digits
    """
    digits_in_keylogs = {}
    for log in keylogs:
        for k in range(len(log)):
            if log[k] not in digits_in_keylogs:
                digits_in_keylogs[log[k]] = set()
            else:
                digits_in_keylogs[log[k]] = digits_in_keylogs[log[k]] | (
                    set(digit for digit in log[k+1:]))
    return digits_in_keylogs


def get_pass(digits_in_keylogs: Dict[str, Set[str]]) -> int:
    """Returns the shortest password resulting from a dicionary of keylogs.

    Args:
        digits_in_keylogs (Dict[str, Set[str]]): Digits in the keylogs and digits that come after them.

    Returns:
        int: The password
    """
    password = []
    while digits_in_keylogs != {}:
        for key in list(digits_in_keylogs.keys()):
            if digits_in_keylogs[key] == set():
                password.append(key)
                del digits_in_keylogs[key]
                for other_keys in digits_in_keylogs.keys():
                    digits_in_keylogs[other_keys].remove(key)

    password = int("".join(list(reversed(password))))
    return password


def process_data(dir: str) -> List[str]:
    with open(dir, 'r') as keylog:
        keylogs = keylog.read().splitlines()
    return keylogs


if __name__ == "__main__":
    result = main()
    print(result)
