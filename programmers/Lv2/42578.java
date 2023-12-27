// [Programmers] 42578. 의상

package programmers.Lv2;

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> clothesMap = new HashMap<>();
        int answer = 1;
        
        for (String[] c: clothes) {
            if (clothesMap.containsKey(c[1])) {
                clothesMap.put(c[1], clothesMap.get(c[1]) + 1);
            } else {
                clothesMap.put(c[1], 1);
            }
        }
        
        for (String clothesType: clothesMap.keySet()) {
            answer *= clothesMap.get(clothesType) + 1;
        }
        
        return answer - 1;
    }
}