-- Lists all the shows from hbtn_0d_tvshows_rate by their rating
-- Records are orderd by descending order
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
