import java.util.*;
import java.io.*;
class _150367 {
    static int[] answer;

    public static boolean make_tree(String elem) {
        boolean check = true;
        int mid = (elem.length() - 1) / 2;
        char root = elem.charAt(mid);
        String left = elem.substring(0, mid);
        String right = elem.substring(mid + 1);
        if (root == '0' && (left.charAt((left.length() - 1) / 2) == '1' || right.charAt((right.length() - 1) / 2) == '1'))
            return false;
        if (left.length() >= 3) {
            check = make_tree(left);
            if (check)
                check = make_tree(right);
        }
        return check;
    }
    public static void main(String[]args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] numbers = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        answer = new int[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            String elem = Long.toBinaryString(numbers[i]);
            int j = 0;
            int target = 1;
            while (target < elem.length()) {
                j++;
                target += (int)Math.pow(2, j);
            }
            while (target > elem.length()) elem = "0" + elem;
            if (make_tree(elem)) answer[i] = 1;
        }
        System.out.println(Arrays.toString(answer));
    }
}