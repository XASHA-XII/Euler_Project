from collections import Counter
import itertools
from typing import Dict, List, Tuple, Type

'''
https://projecteuler.net/problem=54
Poker hands
'''


def main() -> int:
    """The .txt  file consists of 1000 poker games beteen two player. It computes how many hands player one wins.

    Returns:
        int: Number of wins of player1
    """
    DIR = 'data/' + 'p054_poker.txt'

    with open(DIR, 'r') as tournament:
        result = 0
        for game in tournament:
            game = game.replace("\n", "").split(" ")
            hand_1 = Hand(*tuple(Card(x) for x in game[:5]))
            hand_2 = Hand(*tuple(Card(x) for x in game[5:]))
            if hand_1 > hand_2:
                result += 1

    return result


class Card(object):
    SUITS: Dict[str, int] = {'C': 1, 'D': 2, 'H': 3, 'S': 4}
    RANKS: Dict[str, int] = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                             '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, card_str: str) -> None:
        self.rank = Card.RANKS[card_str[0]]
        self.suit = Card.SUITS[card_str[1]]


class Hand(object):

    EVALUTATION: Dict[str, int] = ({'High Card': 1,
                                   'A Pair': 2,
                                    'Two Pairs': 3,
                                    'Three of a Kind': 4,
                                    'Straight': 5,
                                    'Flush': 6,
                                    'Full House': 7,
                                    'Four of a Kind': 8,
                                    'Straight Flush': 9,
                                    'Royal Flush': 10})
    SPECIAL_CASE_STREET: Tuple = (14, 5, 4, 3, 2)

    RANKS: List[int] = list(range(2, 15))

    FIVE_OUT_OF_FIFTEEN: Dict[Tuple[int], int] = {}
    for k, hand in enumerate(itertools.product(RANKS, RANKS, RANKS, RANKS, RANKS)):
        FIVE_OUT_OF_FIFTEEN[hand] = k

    FOUR_OUT_OF_FIFTEEN: Dict[Tuple[int], int] = {}
    for k, hand in enumerate(itertools.product(RANKS, RANKS, RANKS, RANKS)):
        FOUR_OUT_OF_FIFTEEN[hand] = k

    THREE_OUT_OF_FIFTEEN: Dict[Tuple[int], int] = {}
    for k, hand in enumerate(itertools.product(RANKS, RANKS, RANKS)):
        THREE_OUT_OF_FIFTEEN[hand] = k

    TWO_OUT_OF_FIFTEEN: Dict[Tuple[int], int] = {}
    for k, hand in enumerate(itertools.product(RANKS, RANKS)):
        TWO_OUT_OF_FIFTEEN[hand] = k

    def __init__(self, *args) -> None:
        self.ranks = sorted(args, key=lambda x: -x.rank)
        self.evaluation = self.evaluate()

    def __gt__(self, other):
        result = self.evaluation > other.evaluation
        return result

    def evaluate(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        counted_ranks = Counter(ranks)
        if self.has_straight_flush():
            primary = Hand.EVALUTATION['Straight Flush']
            secondary = Hand.rank_straight(ranks)
        elif self.has_four_of_a_kind():
            primary = Hand.EVALUTATION['Four of a Kind']
            secondary = Hand.rank_four_of_a_kind(counted_ranks)
        elif self.has_full_house():
            primary = Hand.EVALUTATION['Full House']
            secondary = Hand.rank_full_house(counted_ranks)
        elif self.has_flush():
            primary = Hand.EVALUTATION['Flush']
            secondary = Hand.rank_flush(ranks)
        elif self.has_straight():
            primary = Hand.EVALUTATION['Straight']
            secondary = Hand.rank_straight(ranks)
        elif self.has_three_of_a_kind():
            primary = Hand.EVALUTATION['Three of a Kind']
            secondary = Hand.rank_three_of_a_kind(counted_ranks)
        elif self.has_two_pairs():
            primary = Hand.EVALUTATION['Two Pairs']
            secondary = Hand.rank_two_pairs(counted_ranks)
        elif self.has_a_pair():
            primary = Hand.EVALUTATION['A Pair']
            secondary = Hand.rank_pair(counted_ranks)
        else:
            primary = Hand.EVALUTATION['High Card']
            secondary = Hand.rank_high_card(ranks)
        self.evaluation = (primary, secondary)
        return self.evaluation

    def has_royal_flush(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        has_straight_flush = self.has_flush()
        high_card_ace = max(
            ranks) == 14 and not ranks == self.SPECIAL_CASE_STREET
        return has_straight_flush and high_card_ace

    def has_straight_flush(self):
        has_straight_flush = self.has_flush() and self.has_straight()
        return has_straight_flush

    def has_four_of_a_kind(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        four_of_a_kind = sum(1 for rank in ranks if ranks.count(rank) == 4)
        return (four_of_a_kind == 4)

    def has_full_house(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        three_of_a_kind = sum(1 for rank in ranks if ranks.count(rank) == 3)
        pairs = sum(1 for rank in ranks if ranks.count(rank) == 2)
        return (three_of_a_kind == 3) and (pairs == 2)

    def has_flush(self):
        _, suits = zip(*[(card.rank, card.suit) for card in self.ranks])
        flush = suits.count(suits[0]) == len(suits)
        return flush

    def has_straight(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        normal_street = all(a == b + 1 for a, b in zip(ranks, ranks[1:]))
        special_street = ranks == self.SPECIAL_CASE_STREET
        return normal_street or special_street

    def has_three_of_a_kind(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        three_of_a_kind = sum(1 for rank in ranks if ranks.count(rank) == 3)
        return (three_of_a_kind == 3)

    def has_two_pairs(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        pairs = sum(1 for rank in ranks if ranks.count(rank) == 2)
        return (pairs == 4)

    def has_a_pair(self):
        ranks, _ = zip(*[(card.rank, card.suit) for card in self.ranks])
        pairs = sum(1 for rank in ranks if ranks.count(rank) == 2)
        return (pairs == 2)

    def has_high_card(self):
        return True

    @staticmethod
    def rank_four_of_a_kind(counted_ranks: Dict[int, int]):
        for key in counted_ranks.keys():
            if counted_ranks[key] == 4:
                quadruplet = key
            else:
                high_card = key
        hand = (quadruplet, high_card)
        return Hand.TWO_OUT_OF_FIFTEEN[hand]

    @staticmethod
    def rank_full_house(counted_ranks: Dict[int, int]):
        for key in counted_ranks.keys():
            if counted_ranks[key] == 3:
                triple = key
            else:
                pair = key
        hand = (triple, pair)
        return Hand.TWO_OUT_OF_FIFTEEN[hand]

    @staticmethod
    def rank_flush(ranks: List[int]):
        return Hand.rank_high_card(ranks)

    @staticmethod
    def rank_straight(ranks: List[int]):
        if ranks == Hand.SPECIAL_CASE_STREET:
            return 5
        else:
            return max(ranks)

    @staticmethod
    def rank_three_of_a_kind(counted_ranks: Dict[int, int]):
        high_card = 0
        for key in counted_ranks.keys():
            if counted_ranks[key] == 3:
                triplet = key
            elif key > high_card:
                high_card = key
            else:
                low_card = key
        hand = (triplet, high_card, low_card)
        return Hand.THREE_OUT_OF_FIFTEEN[hand]

    @staticmethod
    def rank_two_pairs(counted_ranks: Dict[int, int]):
        high_pair = 0
        for key in counted_ranks.keys():
            if counted_ranks[key] == 2 and key > high_pair:
                high_pair = key
            elif counted_ranks[key] == 2:
                low_pair = key
            else:
                low_card = key
        hand = (high_pair, low_pair, low_card)
        return Hand.THREE_OUT_OF_FIFTEEN[hand]

    @staticmethod
    def rank_pair(counted_ranks: Dict[int, int]):
        high_mid_low = tuple(
            rank for rank in counted_ranks.keys() if counted_ranks[rank] == 1)
        for key in counted_ranks.keys():
            if counted_ranks[key] == 2:
                pair = (key,)
        hand = pair + high_mid_low
        return Hand.FOUR_OUT_OF_FIFTEEN[hand]

    @staticmethod
    def rank_high_card(ranks: List[int]):
        return Hand.FIVE_OUT_OF_FIFTEEN[ranks]


if __name__ == '__main__':
    result = main()
    print(result)
