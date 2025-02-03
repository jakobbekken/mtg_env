__version__ = "0.1.0"
__author__ = "Jakob Moen Bekken"
__email__ = "post@jokko.no"

from .environment import GameEnvironment

def start_game():
    env = GameEnvironment()
    env.setup()
    return env
