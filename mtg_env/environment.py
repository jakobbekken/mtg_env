"""
This module defines the game environment simulation. The `GameEnvironment` is the main interface for interacting with the environment.

Classes:
    GameEnvironment: Represents a game, managing players, turns, etc.

Examples:
    game = Game
"""
class GameEnvironment:
    """The GameEnvironment class represents a game, its players, turns, etc.

    Attributes:
        players: The list of current game's players.
    """
    def __init__(self, decks: list[str]):
        """Initializes the instance based on the players.
        
        Args:
            players: Defines this games players, their libraries, life totals, etc.
            active_player: The current turns active players.
        """
        self.players: list[str] = ["p1", "p2"]  # TODO: Make Player object out of decks
        self.active_player: str = self.players[0]
        # TODO: self.stack = Stack()

    def setup(self):
        """Sets up the environment by shuffling libraries and doing muligans.
        
        Returns:
            None
        """
        pass

    def start(self):
        """Starts game.
        
        Returns:
            None
        """
        pass
