import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2559 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int k = Integer.parseInt(stringTokenizer.nextToken());
        int[] temperatures = new int[n];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 0; i < n; i++) {
            temperatures[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        int maxValue = Integer.MIN_VALUE;
        int currValue = 0;
        for (int i = 0; i < k; i++) {
            currValue += temperatures[i];
        }
        if (currValue > maxValue) {
            maxValue = currValue;
        }
        for (int j = k; j < n; j++) {
            int i = j - k;
            currValue += temperatures[j];
            currValue -= temperatures[i];
            if (currValue > maxValue) {
                maxValue = currValue;
            }
        }
        System.out.println(maxValue);
    }
}
