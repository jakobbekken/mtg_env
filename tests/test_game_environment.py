import pytest
from mtg_env.environment import GameEnvironment

def test_initial_state():
    decks = ["d1", "d2"]
    env = GameEnvironment(decks)
    assert env.active_player == "p1"
    assert len(env.players) == 2
