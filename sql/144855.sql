/* [Programmers] 144855. 카테고리 별 도서 판매량 집계하기 */

SELECT BOOK.CATEGORY, SUM(BOOK_SALES.SALES) as TOTAL_SALES
FROM BOOK
INNER JOIN BOOK_SALES
ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE BOOK_SALES.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY BOOK.CATEGORY
ORDER BY BOOK.CATEGORY asc;