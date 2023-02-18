'''
https://projecteuler.net/problem=59
XOR Decryption
'''
import itertools
from typing import List


def main() -> int:
    """Checks all possible keys consisting of three lower case letters decypher a message represented
    by a .txt-file to find the decrypthed message and returns the ascii value of the message. 
    The criteria used to decypher is to look for common English words.

    Returns:
        int: The ascii-value of a message.
    """
    DIR = 'data/' + 'p059_cipher.txt'
    CYPHER = process_data(DIR)
    MOST_COMMON_ENGLISH_WORDS = ["the", "of", "and", "to", "Euler"]

    lc_letters = list(range(ord('a'), ord('x')+1))
    key_gen = itertools.product(lc_letters, lc_letters, lc_letters)

    for key in key_gen:
        message = xor_decypher(CYPHER, key)
        if all(w in message for w in MOST_COMMON_ENGLISH_WORDS):
            print(message)
            return sum(ord(x) for x in message)


def xor_decypher(cypher: List[int], key: List[int]) -> str:
    """Generates a message given a list of ints representing the ascii-values of a cypher and a
    list of int of 3-digit keys representing a lowercase key

    Args:
        cypher (List[int]): The cypher.
        key (List[int]): The key.

    Returns:
        str: The decrypthed message.
    """
    len_cypher = len(cypher)
    len_key = len(key)
    cypher_key = (len_cypher // len_key) * key
    message = "".join(chr(c ^ k) for c, k in zip(cypher, cypher_key))
    return message


def process_data(dir: str) -> List[int]:
    """Turns a txt.file of ints seperated by commas into a list of ints

    Args:
        dir (str): Path to the txt file

    Returns:
        List[int]: list of ints.
    """
    with open(dir, 'r') as cypher:
        cypher = [int(x) for x in cypher.read().split(',')]
        return cypher


if __name__ == '__main__':
    result = main()
    print(result)
