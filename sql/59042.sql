/* [Programmers] 59042. 없어진 기록 찾기 */

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS as OUTS
LEFT JOIN ANIMAL_INS as INS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID;