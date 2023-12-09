/* [Programmers] 59043. 있었는데요 없었습니다 */

SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS as INS
INNER JOIN ANIMAL_OUTS as OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME asc;