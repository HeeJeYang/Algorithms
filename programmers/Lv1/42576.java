// [Programmers] 42576. 완주하지 못한 선수

package programmers.Lv1;

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> participantMap = new HashMap<>();
        
        for (String p: participant) {
            if (participantMap.containsKey(p)) {
                participantMap.put(p, participantMap.get(p) + 1);
            } else {
                participantMap.put(p, 1);
            }
        }
        
        for (String c: completion) {
            participantMap.put(c, participantMap.get(c) - 1);
        }
        
        for (String p: participantMap.keySet()) {
            if (participantMap.get(p).equals(1)) {
                answer = p;
            }
        }
        
        return answer;
    }
}