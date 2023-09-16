import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _15961 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int d = Integer.parseInt(stringTokenizer.nextToken());
        int k = Integer.parseInt(stringTokenizer.nextToken());
        int c = Integer.parseInt(stringTokenizer.nextToken());
        int[] check = new int[d + 1];
        check[c] = 1;
        int[] plates = new int[n];
        for (int i = 0; i < n; i++) {
            plates[i] = Integer.parseInt(bufferedReader.readLine());
        }
        int result = 1;
        for (int i = 0; i < k; i++) {
            if (check[plates[i]] == 0) {
                check[plates[i]] = 1;
                result++;
                continue;
            }
            check[plates[i]]++;
        }
        int cand = result;
        for (int i = 0; i < n; i++) {
            int j = (i + k) % n;
            check[plates[j]]++;
            if (check[plates[j]] == 1) cand++;
            if (check[plates[i]] == 1) cand--;
            check[plates[i]]--;
            if (check[plates[i]] < 0) check[plates[i]] = 0;
            if (result < cand) result = cand;
        }
        System.out.println(result);

    }
}
