DROP VIEW IF EXISTS TOPSCORE;

CREATE VIEW TOPSCORE AS 
SELECT s.game_id    as id,
       g.name       as game_name,
       max(s.score) as score,
       s.name       as player_name
FROM scoreboard_score s,
     scoreboard_game g
WHERE s.game_id = g.id
GROUP by s.game_id;
