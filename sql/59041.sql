/* [Programmers] 59041. 동명 동물 수 찾기 */

SELECT NAME, COUNT(NAME) as COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT > 1
ORDER BY NAME;