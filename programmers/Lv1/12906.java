// [Programmers] 12906. 같은 숫자는 싫어

import java.util.*;

class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int value = -1;
        
        for (int num: arr) {
            if (value != num) {
                answer.add(num);
                value = num;
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}