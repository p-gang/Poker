import pytest

from src.table import Table
from src.player import Player


@pytest.fixture
def table():
    return Table([Player(0, "mash"), Player(1, "serega"), Player(2, "shaeshok")])

def test_change_on_3_player(table):
    table.players[0].small_blind = True
    table.players[1].big_blind = True
    table.change_blind()
    table.change_blind()
    assert table.players[2].small_blind and table.players[0].big_blind


def test_take_blind(table):
    table.take_blind(table.players[1], table.players[0])
    assert table.players[0].money == 1990
    assert table.players[1].money == 1980

def test_random_card(table):
    table.take_card_on_table()
    assert len(table.table_cards) == 1

def test_check_player_cards(table):
    table.take_cards()
    assert len(table.players[0].cards) + len(table.players[1].cards) + len(table.players[2].cards) == 6
