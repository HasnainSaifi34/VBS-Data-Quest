CREATE VIEW bad_psychological_health_frequency AS
SELECT Indian_States, COUNT(*) AS Bad_Psychological_Health_Count
FROM dataquest
WHERE Psychological_Health = 'Bad'
GROUP BY Indian_States;

