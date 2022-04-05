class Solution {
    public int mostWordsFound(String[] sentences) {
        int count = 1;
        int tempcount =1;
        for (int i =0;i<sentences.length;i++){
            for (int x=0;x<sentences[i].length()-1;x++){
                if(sentences[i].charAt(x) == ' '){
                    tempcount++;
                }
            }
            if (tempcount > count){
                    count = tempcount;
                }
                tempcount = 1;
        }
        return count;
    }
}