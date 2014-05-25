from django.db import models


class Game(models.Model):
	
	name = models.CharField(max_length=50)
    
	def __unicode__(self):
		return self.name


class Score(models.Model):
	
	game = models.ForeignKey(Game)
	
	name = models.CharField(max_length=50)
	
	score = models.IntegerField()
	
	def __unicode__(self):
		return "%s's score of %s in %s" % (self.name, self.score,  self.game.name)
"""
        
SELECT score.game_id as id,
       game.name     as game_name, 
       score.name    as player_name,
       tgc.score   as score
       
FROM scoreboard_score score,
     scoreboard_game game

INNER JOIN(
SELECT s.game_id, max(s.score) as score
FROM scoreboard_score s
GROUP by s.game_id) tgc on score.game_id = tgc.game_id

INNER JOIN scoreboard_game
ON score.game_id = game.id

		"""


class TopScoresManager(models.Manager):
    
    def get_top_scores(self):
        return self.raw("""
        
SELECT * from TOPSCORE""")
    
    
    def try_it(self):
        return Score.objects.annotate(max_score=models.Max('score'))
    
class TopScore(models.Model):
    
    objects = TopScoresManager()
	
    game_name = models.CharField(max_length=50)
	
    player_name = models.CharField(max_length=50)
	
    score = models.IntegerField()
	
    
    def __unicode__(self):
        return "{score} in {game} by {name}" \
            .format(
                score=self.score, 
                game=self.game_name, 
                name = self.player_name)
    
    class Meta:
        managed = False


