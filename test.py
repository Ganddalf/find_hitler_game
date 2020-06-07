import unittest
from game import Game, Level

class Test_Game(unittest.TestCase):
    def test_start_game(self):
        game_ = Game()
        self.assertEqual(len(game_.levels), 18)

    def test_level_with_without_gitler(self):
        game_= Game()
        level_ = game_.levels[0] #Germany
        level_.set_table()
        self.assertEqual(level_.links[0], "Гитлер, Адольф")
        level_ = game_.levels[4]  #Moscow
        level_.set_table()
        self.assertNotEqual(level_.links[0], "Гитлер, Адольф")

    def test_clear_game(self):
        game_ = Game()
        levels_start = game_.levels

        game_.clear()
        levels_restart = game_.levels

        self.assertListEqual(levels_restart, levels_start)
        self.assertIsNone(game_.current_level)


if __name__ == 'main':

    unittest.main()