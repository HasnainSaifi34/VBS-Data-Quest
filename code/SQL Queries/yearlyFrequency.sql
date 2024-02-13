CREATE VIEW bad_psychological_health_frequency2017 AS
SELECT Indian_States, COUNT(*) AS Bad_Psychological_Health_Count
FROM dataquest
WHERE Psychological_Health = 'Bad' AND Year=2017
GROUP BY Indian_States;

CREATE VIEW bad_psychological_health_frequency2018 AS
SELECT Indian_States, COUNT(*) AS Bad_Psychological_Health_Count
FROM dataquest
WHERE Psychological_Health = 'Bad' AND Year=2018
GROUP BY Indian_States;

CREATE VIEW bad_psychological_health_frequency2019 AS
SELECT Indian_States, COUNT(*) AS Bad_Psychological_Health_Count
FROM dataquest
WHERE Psychological_Health = 'Bad' AND Year=2019
GROUP BY Indian_States;

CREATE VIEW bad_psychological_health_frequency2020 AS
SELECT Indian_States, COUNT(*) AS Bad_Psychological_Health_Count
FROM dataquest
WHERE Psychological_Health = 'Bad' AND Year=2020
GROUP BY Indian_States;