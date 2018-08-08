import pytest
from src import Card
from src.checker import Checker


@pytest.fixture
def checker():
    return Checker


def test_is_free(checker):
    hand = [Card(4, 'Spades'), Card(10, 'Spades')]
    cards = (Card(10, 'Hearts'), Card(10, "Diamonds"), Card(2, 'Diamonds'), Card(3, 'Diamonds'))
    assert checker.is_free(hand, cards) == (3, 10)
