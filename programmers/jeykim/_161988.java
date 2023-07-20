public class _161988 {
    public static void main(String[] args) {
        int[] sequence = new int[]{2, 3, -6, 1, 3, -1, 2, 4};
        long answer = 0;
        int[] pos_seq = new int[sequence.length];
        int[] neg_seq = new int[sequence.length];
        long[][] dp = new long[sequence.length][2];
        int pulse = 1;
        for (int i = 0; i < sequence.length; i++) {
            pos_seq[i] = sequence[i] * pulse;
            pulse *= -1;
            neg_seq[i] = sequence[i] * pulse;
        }
        dp[0][0] = sequence[0];
        dp[0][1] = -sequence[0];
        answer = Math.max(dp[0][0], dp[0][1]);
        long tmp;
        for (int i = 1; i < sequence.length; i++) {
            dp[i][0] = Math.max(pos_seq[i], dp[i - 1][0] + pos_seq[i]);
            dp[i][1] = Math.max(neg_seq[i], dp[i - 1][1] + neg_seq[i]);
            tmp = Math.max(dp[i][0], dp[i][1]);
            answer = Math.max(answer, tmp);
        }
        System.out.println(answer);
    }
}
