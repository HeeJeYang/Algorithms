# [Programmers] 135807. 숫자 카드 나누기
# 소요 시간 : 40분

def solution(arrayA, arrayB):
    
    # 최대공약수 구하는 함수
    def GCD(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    # 두 조건 중 하나를 만족
    def chk(arrayA, arrayB):
        
        # arrayA의 모든 원소들의 GCD 구하기
        a_gcd = arrayA[0]
        for i in range(1, len(arrayA)):
            a_gcd = GCD(a_gcd, arrayA[i])
            if a_gcd == 1:
                return 0
            
        # 공약수들을 찾아 조건에 부합하는지 확인
        for i in range(1, a_gcd // 2 + 1):
            if a_gcd % i == 0:
                divisor = a_gcd // i  # 공약수
                
                for j in arrayB:
                    # 하나라도 나누어 떨어지는 경우가 있다면 제외
                    if j % divisor == 0:
                        break
                
                # divisor가 arrayB의 모든 원소에 대해 나누어 떨어지지 않을 때
                else:
                    return divisor

        return 0
    
    return max(chk(arrayA, arrayB), chk(arrayB, arrayA))