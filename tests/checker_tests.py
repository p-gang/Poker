import pytest
from src.card import Card
from src.checker import Checker


@pytest.fixture
def checker():
    return Checker()


def test_is_pair(checker):
    hand = [Card(4, 'Spades'), Card(6, 'Spades')]
    cards = [Card(10, 'Hearts'), Card(10, "Diamonds"), Card(2, 'Diamonds'), Card(3, 'Diamonds')]
    assert checker.is_pair(hand, cards) == (1, 10)


def test_is_two_pair(checker):
    hand = [Card(2, 'Spades'), Card(6, 'Spades')]
    cards = [Card(10, 'Hearts'), Card(10, "Diamonds"), Card(2, 'Diamonds'), Card(6, 'Diamonds')]
    assert checker.is_two_pair(hand, cards) == [2, 10, 6]


def test_is_three(checker):
    hand = [Card(4, 'Spades'), Card(10, 'Spades')]
    cards = [Card(10, 'Hearts'), Card(10, "Diamonds"), Card(2, 'Diamonds'), Card(3, 'Diamonds')]
    assert checker.is_three(hand, cards) == (3, 10)


def test_is_straight(checker):
    hand = [Card(5, 'Spades'), Card(6, 'Spades')]
    cards = [Card(4, 'Hearts'), Card(7, "Diamonds"), Card(3, 'Spades'), Card(3, 'Diamonds')]
    assert checker.is_straight(hand, cards) == (4, 7)


def test_is_straight_start_from_ace(checker):
    hand = [Card(14, 'Spades'), Card(9, 'Spades')]
    cards = [Card(2, 'Hearts'), Card(3, "Diamonds"), Card(4, 'Diamonds'), Card(1, 'Diamonds')]
    assert checker.is_straight(hand, cards) == (4, 4)


def test_is_straight_with_four_cards(checker):
    hand = [Card(13, 'Spades'), Card(9, 'Spades')]
    cards = [Card(2, 'Hearts'), Card(3, "Diamonds"), Card(5, 'Diamonds'), Card(1, 'Diamonds')]
    assert checker.is_straight(hand, cards) is None


def test_is_flush(checker):
    hand = [Card(14, 'Spades'), Card(9, 'Spades')]
    cards = [Card(2, 'Spades'), Card(3, "Spades"), Card(4, 'Spades'), Card(1, 'Diamonds')]
    assert checker.is_flush(hand, cards) == (5, 'Spades')


def test_is_full_house(checker):
    hand = [Card(2, 'Diamons'), Card(9, 'Spades')]
    cards = [Card(2, 'Spades'), Card(9, "Hearts"), Card(9, 'Clubs'), Card(1, 'Diamonds')]
    assert checker.is_full_house(hand, cards) == (6, 2, 9)


def test_is_full_house_not_three(checker):
    hand = [Card(4, 'Spades'), Card(10, 'Spades')]
    cards = [Card(10, 'Hearts'), Card(10, "Diamonds"), Card(2, 'Diamonds'), Card(3, 'Diamonds')]
    assert checker.is_full_house(hand, cards) is None


def test_is_four(checker):
    hand = [Card(10, 'Clubs'), Card(10, 'Spades')]
    cards = [Card(10, 'Hearts'), Card(10, "Diamonds"), Card(2, 'Diamonds'), Card(3, 'Diamonds')]
    assert checker.is_four(hand, cards) == (7, 10)


def test_is_straight_flush(checker):
    hand = [Card(5, 'Hearts'), Card(6, 'Hearts')]
    cards = [Card(4, 'Hearts'), Card(7, "Hearts"), Card(3, 'Hearts'), Card(8, 'Diamonds')]
    assert checker.is_straight_flush(hand, cards) == (8, 7)


def test_is_straight_flush_start_from_ace(checker):
    hand = [Card(3, 'Hearts'), Card(4, 'Hearts')]
    cards = [Card(2, 'Hearts'), Card(14, "Hearts"), Card(1, 'Hearts'), Card(8, 'Diamonds')]
    assert checker.is_straight_flush(hand, cards) == (8, 4)


def test_is_straight_flush_with_four_cards(checker):
    hand = [Card(3, 'Hearts'), Card(4, 'Hearts')]
    cards = [Card(2, 'Hearts'), Card(13, "Hearts"), Card(1, 'Hearts'), Card(8, 'Diamonds')]
    assert checker.is_straight_flush(hand, cards) is None


def test_is_flush_royal(checker):
    hand = [Card(14, 'Hearts'), Card(13, 'Hearts')]
    cards = [Card(12, 'Hearts'), Card(11, "Hearts"), Card(10, 'Hearts'), Card(8, 'Diamonds')]
    assert checker.is_flush_royal(hand, cards) == 9
