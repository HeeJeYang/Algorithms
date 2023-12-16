/* [Programmers] 59044. 오랜 기간 보호한 동물(1) */

SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS as INS
LEFT JOIN ANIMAL_OUTS as OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
LIMIT 3;