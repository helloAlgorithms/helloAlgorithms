import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2167 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        int[][] s = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            String[] charArray = bufferedReader.readLine().split(" ");
            for (int j = 1; j <= m; j++) {
                s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + Integer.parseInt(charArray[j - 1]);
            }
        }
        int k = Integer.parseInt(bufferedReader.readLine());
        for (int c = 0; c < k; c++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int i = Integer.parseInt(stringTokenizer.nextToken());
            int j = Integer.parseInt(stringTokenizer.nextToken());
            int x = Integer.parseInt(stringTokenizer.nextToken());
            int y = Integer.parseInt(stringTokenizer.nextToken());

            System.out.println(s[x][y] - s[x][j - 1] - s[i - 1][y] + s[i - 1][j - 1]);
        }
    }
}