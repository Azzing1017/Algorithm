-- 코드를 작성해주세요
SELECT A.ID, A.EMAIL, A.FIRST_NAME, A.LAST_NAME
FROM DEVELOPERS AS A
WHERE
    A.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME LIKE 'Python') > 0
    OR A.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME LIKE 'C#') > 0
ORDER BY A.ID ASC;








# SELECT DISTINCT(A.ID), A.EMAIL, A.FIRST_NAME, A.LAST_NAME
# FROM DEVELOPERS AS A, SKILLCODES AS B
# WHERE (A.SKILL_CODE & B.CODE) > 0 AND B.NAME IN ('Python', 'C#')
# ORDER BY A.ID ASC;