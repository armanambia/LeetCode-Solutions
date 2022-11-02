
class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!=t.length()){
            return false;
        }

        Map<Character, Integer> occur = new HashMap<>();

        for(char x : s.toCharArray()){
            if(occur.containsKey(x)){
                occur.put(x, occur.get(x)+1);
            } else{
                occur.put(x, 1);
            }
        }

        for(char x : t.toCharArray()){
            if(!occur.containsKey(x) || occur.get(x)<=0){
                return false;
            } else{
                occur.put(x, occur.get(x)-1);
            }
        }

        return true;
        
    }
}