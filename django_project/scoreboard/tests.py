from django.test import TestCase
from scoreboard.models import Game, Score, TopScore

class ATestCase(TestCase):

    def setUp(self):

        # Create two games.
        self._ddr = Game(name="DDR")
        self._pacman = Game(name="Pac-Man")

        self._ddr.save()
        self._pacman.save()

        # Create four scores.
        Score(game = self._ddr, name="QBRT", score=50001).save()
        Score(game = self._ddr, name="Sonic", score=50020).save()
        
        Score(game = self._ddr, name="Luigi", score=802302).save()
        Score(game = self._ddr, name="Mario", score=38834).save()
        Score(game = self._pacman, name="Kong", score=30002).save()
        Score(game = self._pacman, name="FLOP", score=12345).save()

    def test_custom_query(self):
        
        # Act
        ts = TopScore.objects.get_top_scores()
        ts = list(ts)
        
        # Asserts
        game_names = [topscore.game_name for topscore in ts]

        self.assertTrue("DDR" in game_names)
        self.assertTrue("Pac-Man" in game_names)
        
        query_count = len([p for p in ts 
            if p.player_name == "Luigi" 
            and p.game_name == "DDR"])
        self.assertEqual(query_count, 1,
            "Luigi should be the top score for DDR")
            
        query_count = len([p for p in ts 
            if p.player_name == "Kong" 
            and p.game_name == "Pac-Man"])
        self.assertEqual(query_count, 1,
            "Kong should be the top score for Pac-Man")
