SELECT traffic_source, COUNT(*) AS users
FROM web_analytics
GROUP BY traffic_source;

SELECT traffic_source, AVG(conversion) AS conversion_rate
FROM web_analytics
GROUP BY traffic_source;

SELECT AVG(sessions) AS avg_sessions
FROM web_analytics;
