-- compute the number of occurence of certain score
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER by number DESC;
