import java.util.*;
class _25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tot = sc.nextInt();
        int cnt = sc.nextInt();
        int t = 0;
        while (cnt-- > 0) {
            t += sc.nextInt() * sc.nextInt();
        }
        if (t == tot) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}