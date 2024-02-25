-- 코드를 입력하세요
WITH A AS (
    SELECT DISTINCT(CART_ID)
    FROM CART_PRODUCTS 
    WHERE NAME = 'Milk'
),
B AS (
    SELECT DISTINCT(CART_ID)
    FROM CART_PRODUCTS
    WHERE NAME = 'Yogurt'
)

SELECT A.CART_ID
FROM A
    INNER JOIN B
    ON A.CART_ID = B.CART_ID
ORDER BY A.CART_ID ASC;


