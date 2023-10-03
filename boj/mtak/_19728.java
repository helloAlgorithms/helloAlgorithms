import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _19728 {

  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
    int n = Integer.parseInt(stringTokenizer.nextToken());
    int m = Integer.parseInt(stringTokenizer.nextToken());
    int[] rowCount = new int[m + 1];
    for (int c = 0; c < n; c++) {
      stringTokenizer = new StringTokenizer(bufferedReader.readLine());
      for (int _m = 1; _m <= m; _m++) {
        rowCount[_m] += Integer.parseInt(stringTokenizer.nextToken());
      }
    }
    int[] acc = new int[m + 1];
    for (int i = 1; i <= m; i++) {
      acc[i] = acc[i - 1] + rowCount[i];
    }
    int a = Integer.parseInt(bufferedReader.readLine());
    int ret = acc[a] - acc[0];
    int curr = ret;
    int endIdx = a;
    while (endIdx < m) {
      endIdx++;
      int cand = acc[endIdx] - acc[endIdx - a];
      if (ret < cand) {
        ret = cand;
      }
    }
    System.out.println(ret);
  }
}
