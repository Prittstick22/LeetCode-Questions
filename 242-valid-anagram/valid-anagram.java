class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> Hs1=new HashMap<Character,Integer>();
        HashMap<Character,Integer> Hs2=new HashMap<Character,Integer>();
        if(s.length()!=t.length()) return false;    
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            Hs1.put(ch,(Hs1.getOrDefault(ch,0))+1);
        }
        for(int i=0;i<t.length();i++){
            char ch=t.charAt(i);
            Hs2.put(ch, Hs2.getOrDefault(ch, 0) + 1);
        }
        if(Hs1.equals(Hs2)){
            return true;
        }
        return false;
    }
}