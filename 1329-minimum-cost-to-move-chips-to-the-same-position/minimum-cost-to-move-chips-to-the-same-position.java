class Solution {
    public int minCostToMoveChips(int[] position) {
        int o = 0;
        int e = 0;
        for(int i = 0; i < position.length; i++) {
            if(position[i] % 2 == 0) {
                e++;
            } else {
                o++;
            }
        }
        
        return Math.min(o, e);
    }
}