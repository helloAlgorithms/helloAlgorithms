import java.util.*;
import java.util.stream.*;
class _25314 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tot = sc.nextInt();
        System.out.println(Stream.generate(()->"long ").limit(Math.round(tot / 4)).reduce((a, b) -> a + b).get() +"int");
    }
}