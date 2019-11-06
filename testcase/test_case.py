import unittest
from multiplayer import Mulitplayer
from singleplayer import Singleplayer
from tacticalplayer import Tacticalplayer


class TestCase(unittest.TestCase):

    def setUp(self):
        self.people_message = 'Game over! You win the game!'
        self.computer_message = 'Game over! Computer wins the game!'
        self.even_message = 'Game over! Even'
        self.round_people_message = 'You win this round!'
        self.round_computer_message = 'Computer wins this round!'
        self.round_even_message = 'Even'
        self.player_1_message = 'Game over! Player1 win the game!'
        self.player_2_message = 'Game over! Player2 win the game!'

        print("setup method execute")

    def test_singleplay(self):
        msg0 = Singleplayer.win(self, 0, 0, 3)
        self.assertEqual(msg0, self.even_message)
        msg1 = Singleplayer.win(self, 1, 1, 1)
        self.assertEqual(msg1, self.even_message)
        msg2 = Singleplayer.win(self, 2, 1, 0)
        self.assertEqual(msg2, self.people_message)
        msg3 = Singleplayer.win(self, 3, 0, 0)
        self.assertEqual(msg3, self.people_message)
        msg4 = Singleplayer.win(self, 2, 0, 1)
        self.assertEqual(msg4, self.people_message)
        msg5 = Singleplayer.win(self, 1, 2, 0)
        self.assertEqual(msg5, self.computer_message)
        msg6 = Singleplayer.win(self, 0, 3, 0)
        self.assertEqual(msg6, self.computer_message)
        msg7 = Singleplayer.win(self, 0, 2, 1)
        self.assertEqual(msg7, self.computer_message)

    def test_mulitplay(self):
        msg10 = Mulitplayer.win(self, 0, 0, 3)
        self.assertEqual(msg10, self.even_message)
        msg11 = Mulitplayer.win(self, 1, 1, 1)
        self.assertEqual(msg11, self.even_message)
        msg12 = Mulitplayer.win(self, 2, 1, 0)
        self.assertEqual(msg12, self.player_1_message)
        msg13 = Mulitplayer.win(self, 3, 0, 0)
        self.assertEqual(msg13, self.player_1_message)
        msg14 = Mulitplayer.win(self, 2, 0, 1)
        self.assertEqual(msg14, self.player_1_message)
        msg15 = Mulitplayer.win(self, 1, 2, 0)
        self.assertEqual(msg15, self.player_2_message)
        msg16 = Mulitplayer.win(self, 0, 3, 0)
        self.assertEqual(msg16, self.player_2_message)
        msg17 = Mulitplayer.win(self, 0, 2, 1)
        self.assertEqual(msg17, self.player_2_message)

    def test_tacticalplay(self):
        msg18 = Tacticalplayer.win(self, 0, 0, 3)
        self.assertEqual(msg18, self.even_message)
        msg19 = Tacticalplayer.win(self, 1, 1, 1)
        self.assertEqual(msg19, self.even_message)
        msg20 = Tacticalplayer.win(self, 2, 1, 0)
        self.assertEqual(msg20, self.people_message)
        msg21 = Tacticalplayer.win(self, 3, 0, 0)
        self.assertEqual(msg21, self.people_message)
        msg22 = Tacticalplayer.win(self, 2, 0, 1)
        self.assertEqual(msg22, self.people_message)
        msg23 = Tacticalplayer.win(self, 1, 2, 0)
        self.assertEqual(msg23, self.computer_message)
        msg24 = Tacticalplayer.win(self, 0, 3, 0)
        self.assertEqual(msg24, self.computer_message)
        msg25 = Tacticalplayer.win(self, 0, 2, 1)
        self.assertEqual(msg25, self.computer_message)

    def tearDown(self):
        print("TearDown method execute")


if __name__ == '__main__':
    unittest.main()
