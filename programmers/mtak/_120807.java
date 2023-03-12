class Solution {
    public int solution(int num1, int num2) {
        return (num1 == num2)? 1:-1;
    }
}

public class _120807 {
    public static void main (String []av) {
        Solution sol = new Solution();
        int solution = sol.solution(11, 11);
        System.out.println("solution = " + solution);
    }
}