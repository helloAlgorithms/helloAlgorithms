import java.util.Scanner;
import java.util.Stack;

public class _9012 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < t; i++) {
            Stack<String> stack = new Stack<>();
            char[] s = scanner.nextLine().toCharArray();
            boolean flag = false;
            for (char c : s) {
                if (c == '(') {
                    stack.push(String.valueOf(c));
                } else {
                    if (stack.isEmpty()) {
                        flag = true;
                        break;
                    }
                    stack.pop();
                }
            }
            if (!stack.isEmpty() || flag) {
                System.out.println("NO");
                continue;
            }
            System.out.println("YES");
        }
    }
}
