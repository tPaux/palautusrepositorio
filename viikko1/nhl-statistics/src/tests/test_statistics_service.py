import unittest

from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    # 4+12   = 16
            Player("Lemieux", "PIT", 45, 54),       # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),          # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),    # 42+56  = 98
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Gretzky")

        self.assertIsNone(player)

    def test_team_returns_only_players_from_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 2)

        names = [player.name for player in players]

        self.assertIn("Kurri", names)
        self.assertIn("Semenko", names)

    def test_top_returns_players_in_correct_order(self):
        top_players = self.stats.top(2)

        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")

    def test_top_by_assists(self):
        print(players[0].name, players[0].goals, players[0].assists, players[0].points)
        players = self.stats.top(3, SortBy.ASSISTS)

        for p in players:
            print(p.name, p.assists)

    def test_top_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(players[0].goals, 45)
        self.assertEqual(players[1].goals, 42)
        self.assertEqual(players[2].goals, 37)

    def test_top_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(players[0].assists, 56)
        self.assertEqual(players[1].assists, 54)
        self.assertEqual(players[2].assists, 53)

    def test_top_by_points(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")


