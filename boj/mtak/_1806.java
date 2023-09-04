import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1806 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        long s = Integer.parseInt(stringTokenizer.nextToken());
        int[] sumArr = new int[n + 1];
        sumArr[0] = 0;
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 1; i <= n; i++) {
            sumArr[i] = sumArr[i - 1] + Integer.parseInt(stringTokenizer.nextToken());
        }
//        out : while (ret <= n - 1) {
//            ret += 1;
//            for (int i = 1; i + ret <= n; i++) {
//                if (sumArr[i + ret] - sumArr[i - 1] >= s)break out;
//            }
//        }
        int start_idx = 1;
        int end_idx = 1;
        int min_len = Integer.MAX_VALUE;
        while (end_idx <= n) {
            int sum = sumArr[end_idx] - sumArr[start_idx - 1];
            if (sum >= s) {
                if (min_len > end_idx - start_idx + 1) min_len = end_idx - start_idx + 1;
                start_idx++;
            } else {
                end_idx++;
            }
        }
        if (min_len == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(min_len);
        }
    }
}
