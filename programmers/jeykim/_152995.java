import java.util.*;
public class _152995 {
    public static void main(String[] args) {
        int[][] scores = new int[][]{{2, 2}, {1, 4}, {3, 2}, {3, 2}, {2, 1}};
        int[] target = scores[0];
        int t_sum = target[0] + target[1];
        Arrays.sort(scores, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] != o2[0]) return o2[0] - o1[0];
                else return o1[1] - o2[1];
            }
        });
        int answer = 1;
        int compare = 0;
        for (int i = 0; i < scores.length; i++) {
            int sum = scores[i][0] + scores[i][1];
            if (compare > scores[i][1]) {
                if (scores[i].equals(target)) {
                    answer = -1;
                    break;
                }
            }
            else {
                if (scores[i][1] > compare) compare = scores[i][1];
                if (sum > t_sum) answer++;
            }
        }
        System.out.println(answer);
    }
}
