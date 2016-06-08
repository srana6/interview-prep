class Pramp {
   public static String getSmallestSubstringAllCharacters(String string, char[] uniquechars){
      if (string == null || uniquechars == null || string.length() < uniquechars.length )
         return "";
      
      HashMap<Character, Integer> frequencies = new HashMap<Character, Integer>();
      for (int i = 0; i < uniquechars.length; i++){
         frequences.set(uniquechars[i], 0);
      }
      
      int[] smallestSubstringIdx = {0, 0};      
      int count = 0;
      int i = 0;
      int j = 0;
      
      // O (n)
      // O(m)
      
      while ( j < string.length() ){
         char elem = string.charAt(j);         
         if (frequencies.containsKey(elem)){
            frequencies.set(elem,  frequencies.get(elem) + 1);
            if(frequencies.get(elem) == 1){
               count += 1;
            }
            
                                    
            // shrink
            while (count == uniquechars.length){
               int smallest_size = smallestSubstringIdx[1] - smallestSubstringIdx[0];
               
               if (j - i < smallest_size)
                  smallestSubstringIdx = [i, j];               
               
               char elemBeginning = string.charAt(i);
               
               frequencies.set(elem,  frequencies.get(elem) - 1);
               if(frequencies.get(elem) == 0){
                  count -= 1;
               }   
               i++;
            }                   
         }
         j ++;
      }
      
      return string.substring(smallestSubstringIdx[0], smallestSubstringIdx[1]);
   }
   
   public static void main(String[] args) {
      String pramp = "Practice Makes Perfect";
      System.out.println(pramp);
   }
}