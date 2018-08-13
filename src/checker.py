from operator import attrgetter
from itertools import groupby


class Checker:

    def is_pair(self, hand, cards):
        ranks = [x.get_rank() for x in hand + cards]

        for i in range(14, 0, -1):
            if ranks.count(i) == 2:
                return 1, i
        return None

    def is_two_pair(self, hand, cards):
        ranks = [x.get_rank() for x in hand + cards]
        pair_ranks = []

        for i in range(14, 0, -1):
            if ranks.count(i) == 2:
                pair_ranks.append(i)
            if len(pair_ranks) == 2:
                return [2, ] + pair_ranks
        return self.is_pair(hand, cards)

    def is_three(self, hand, cards):
        ranks = [x.get_rank() for x in hand + cards]

        for i in range(14, 0, -1):
            if ranks.count(i) == 3:
                return 3, i
        return self.is_two_pair(hand, cards)

    def is_straight(self, hand, cards):
        ranks = [x.get_rank() for x in hand + cards]

        if 14 in ranks:
            ranks.append(0)
        sorted_ranks = sorted(set(ranks))

        max_rank = self.check_straight(sorted_ranks)

        if max_rank is not None:
            return 4, max_rank
        return self.is_three(hand, cards)

    def is_flush(self, hand, cards):
        suits = [x.get_suit() for x in hand + cards]

        for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
            if suits.count(suit) == 5:
                return 5, suit
        return self.is_straight(hand, cards)

    def is_full_house(self, hand, cards):
        ranks = [x.get_rank() for x in hand + cards]
        pair_rank = -1

        for i in range(14, 0, -1):
            if ranks.count(i) == 2:
                pair_rank = i

        for i in range(14, 0, -1):
            if ranks.count(i) == 3 and i != pair_rank and pair_rank != -1:
                return (6, pair_rank, i)
        return self.is_flush(hand,cards)

    def is_four(self, hand, cards):
        ranks = [x.get_rank() for x in hand + cards]

        for i in range(14, 0, -1):
            if ranks.count(i) == 4:
                return 7, i
        return self.is_full_house(hand, cards)

    def is_straight_flush(self, hand, cards):
        hearts, spades, diamonds, clubs = self.separate_ranks_by_suits(hand, cards)

        for suit in (hearts, spades, diamonds, clubs):
            if 14 in suit:
                suit.append(0)
            sorted_suit = sorted(suit)

            max_rank = self.check_straight(sorted_suit)

            if max_rank is not None:
                return 8, max_rank
        return self.is_four(hand, cards)

    def is_flush_royal(self, hand, cards):
        hearts, spades, diamonds, clubs = self.separate_ranks_by_suits(hand, cards)

        for suit in (hearts, spades, diamonds, clubs):
            if 14 in suit:
                suit.append(0)
            sorted_suit = sorted(suit)

            max_rank = self.check_straight(sorted_suit)

            if max_rank == 14:
                return 9
        return self.is_straight_flush(hand, cards)

    def separate_ranks_by_suits(self, hand, cards):
        hearts, spades, diamonds, clubs = [], [], [], []

        for card in hand + cards:
            if card.get_suit() == 'Hearts':
                hearts.append(card.get_rank())
            if card.get_suit() == 'Spades':
                spades.append(card.get_rank())
            if card.get_suit() == 'Diamonds':
                diamonds.append(card.get_rank())
            if card.get_suit() == 'Clubs':
                clubs.append(card.get_rank())

        return hearts, spades, diamonds, clubs

    def check_straight(self, sorted_suit):
        for k, g in groupby(enumerate(sorted_suit), lambda x: x[0] - x[1]):
            items = [i[1] for i in g]

            if len(items) >= 5:
                return items[-1]
        return None

    def find_combination(self, hand, cards):
        return self.is_flush_royal(hand, cards)