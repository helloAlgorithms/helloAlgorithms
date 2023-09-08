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
        int[][] sumArr = new int[n + 1][n + 1];
        for (int r = 1; r <= n; r++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int c = 1; c <= n; c++) {
                sumArr[r][c] = sumArr[r][c - 1] + sumArr[r - 1][c] - sumArr[r - 1][c - 1] + Integer.parseInt(stringTokenizer.nextToken());
            }
        }
        for (int i = 0; i < m; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int ret = 0;
            int fx = Integer.parseInt(stringTokenizer.nextToken());
            int fy = Integer.parseInt(stringTokenizer.nextToken());
            int tx = Integer.parseInt(stringTokenizer.nextToken());
            int ty = Integer.parseInt(stringTokenizer.nextToken());
            ret = sumArr[tx][ty] - sumArr[fx - 1][ty] - sumArr[tx][fy - 1] + sumArr[fx - 1][fy - 1];
            System.out.println(ret);
        }
    }
}
