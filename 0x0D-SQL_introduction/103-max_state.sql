-- displays the max temperature of each state (ordered by State name)
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `STATE`
ORDER BY `STATE`;
