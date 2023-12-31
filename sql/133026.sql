/* [Programmers] 133026. 성분으로 구분한 아이스크림 총 주문량 */

SELECT INFO.INGREDIENT_TYPE, SUM(HALF.TOTAL_ORDER) as TOTAL_ORDER
FROM FIRST_HALF as HALF
INNER JOIN ICECREAM_INFO as INFO
ON HALF.FLAVOR = INFO.FLAVOR
GROUP BY INFO.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER asc;