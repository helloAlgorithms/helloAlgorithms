import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        int[] sumArr = new int[n * n + 1];
        sumArr[0] = 0;
        for (int i = 1; i < n+1 ; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int j = 1; j < n + 1; j++) {
                sumArr[(i - 1) * n + j] = sumArr[(i - 1) * n + j - 1] + Integer.parseInt(stringTokenizer.nextToken());
            }
        }
        for (int i = 0; i < m; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int ret = 0;
            int fx = Integer.parseInt(stringTokenizer.nextToken());
            int fy = Integer.parseInt(stringTokenizer.nextToken());
            int tx = Integer.parseInt(stringTokenizer.nextToken());
            int ty = Integer.parseInt(stringTokenizer.nextToken());
            for (int r = fx; r <= tx; r++) {
                ret += sumArr[(r - 1) * n + ty] - sumArr[(r - 1) * n + fy - 1];
            }
            System.out.println(ret);
        }
    }
}
