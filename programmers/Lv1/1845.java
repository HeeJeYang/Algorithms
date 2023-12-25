// [Programmers] 1845. 폰켓몬

package programmers.Lv1;

import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> phonekemonSet = new HashSet<>();
        
        for (int num: nums) {
            phonekemonSet.add(num);
        }
        
        if (nums.length / 2 >= phonekemonSet.size()) {
            answer = phonekemonSet.size();
        } else {
            answer = nums.length / 2;
        }
        
        return answer;
    }
}