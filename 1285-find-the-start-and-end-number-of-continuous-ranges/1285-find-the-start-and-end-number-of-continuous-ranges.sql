# Write your MySQL query statement below


SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
# SELECT log_id, log_id - pre_gap AS diff
# {"headers": ["log_id", "diff"], "values": [[1, 0], [2, 0], [3, 0], [7, 3], [8, 3], [10, 4]]}
FROM (SELECT ROW_NUMBER() OVER(ORDER BY log_id) AS pre_gap,
            log_id
      FROM Logs) t
GROUP BY log_id - pre_gap
ORDER BY start_id