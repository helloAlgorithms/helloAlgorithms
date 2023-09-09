import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class _2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int[] arr = new int[n + 2];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        int startIdx = 1;
        int endIdx = 1;
        int sum = arr[1];
        int cnt = 0;
        while (endIdx != n + 1) {
            if (sum > m) {
                sum -= arr[startIdx];
                startIdx++;
            } else {
                if (sum == m) {
                    cnt++;
                }
                endIdx++;
                sum += arr[endIdx];
            }
        }
        System.out.println(cnt);
    }
}
