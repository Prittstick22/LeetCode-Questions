public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        double ans = 0;
        int[] combind = nums1.Concat(nums2).ToArray();
        Array.Sort(combind);
        int len = combind.Length;

        if (len == 1){
            ans = Convert.ToDouble(combind[0]);
        }

        if (len == 0){
            return ans;
        }
        
        if (len % 2 == 1){
            ans = Convert.ToDouble(combind[(len - 1) /2]);
            
        }
        else{
            ans = Convert.ToDouble(((combind[(len/2) - 1] + combind[len/2])) /2.0);
        }
        return ans;
    }
}