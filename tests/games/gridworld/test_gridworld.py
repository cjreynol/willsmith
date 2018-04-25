from tests.games.game_testcase import GameTestCase

from games.gridworld.grid import Grid
from games.gridworld.gridworld import Gridworld
from games.gridworld.gridworld_action import GridworldAction
from games.gridworld.gridworld_direction import GridworldDirection
from games.gridworld.gridworld_examples import *


class TestGridworld(GameTestCase):
    
    def setUp(self):
        super().setUp()
        self.game = Gridworld(Grid(simple_terminals, 0, simple_walls, (4,3)), 
                                deterministic_transition, (0, 0))
        self.test_action = GridworldAction(GridworldDirection.UP)

    def test_game_equality(self):
        self._test_game_equality()

    def test_last_position_stays_in_sync(self):
        self.assertIsNone(self.game.last_player_pos)
        self.game.take_action(self.test_action)
        self.assertEqual(self.game.last_player_pos, (0, 0))
