-- 코드를 입력하세요
SELECT A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, SUM(C.COUNT * A.PRICE) AS TOTAL_SALES
FROM BOOK AS A
    INNER JOIN AUTHOR AS B
    ON A.AUTHOR_ID = B.AUTHOR_ID
    INNER JOIN (
        SELECT BOOK_ID, SUM(SALES) AS COUNT
        FROM BOOK_SALES
        WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-01'
        GROUP BY BOOK_ID
    ) AS C
    ON A.BOOK_ID = C.BOOK_ID
GROUP BY A.AUTHOR_ID, A.CATEGORY
ORDER BY A.AUTHOR_ID ASC, A.CATEGORY DESC