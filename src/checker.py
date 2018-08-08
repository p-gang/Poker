from operator import attrgetter


class Checker:

    def __init__(self):
        pass

    def is_free(self, hand, cards):
        sorted_cards = sorted(hand+cards, key=attrgetter('rank'), reverse=True)

        for i in range(14, -1, 1):
            if sorted_cards.count(i) == 3:
                return 3, i





