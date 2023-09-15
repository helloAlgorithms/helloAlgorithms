import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class _12891 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int s = Integer.parseInt(stringTokenizer.nextToken());
        int p = Integer.parseInt(stringTokenizer.nextToken());
        int result = 0;
        HashMap<String, Integer> checking = new HashMap<>();
        HashMap<String, Integer> status = new HashMap<>();
        char[] set = bufferedReader.readLine().toCharArray();
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        List<String> list = Arrays.asList("ACGT".split(""));
        for (int i = 0; i < 4; i++) {
            int value = Integer.parseInt(stringTokenizer.nextToken());
            checking.put(list.get(i), value);
            status.put(list.get(i), 0);
        }
        for (int i = 0; i < p; i++) {
            String key = String.valueOf(set[i]);
            status.put(key, status.get(key) + 1);
        }
        result = getResult(result, checking, status, list);
        for (int j = p; j < s; j++) {
            int i = j - p;
            status.put(String.valueOf(set[j]), status.get(String.valueOf(set[j])) + 1);
            status.put(String.valueOf(set[i]), status.get(String.valueOf(set[i])) - 1);
            result = getResult(result, checking, status, list);
        }
        System.out.println(result);
        bufferedReader.close();
    }

    private static int getResult(int result, HashMap<String, Integer> checking, HashMap<String, Integer> status, List<String> list) {
        for (int i = 0; i < 4; i++) {
            if (status.get(list.get(i)) < checking.get(list.get(i))) {
                return result;
            }
        }
        return ++result;
    }
}
