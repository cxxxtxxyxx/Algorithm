
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();

        for (int i = 0; i < T; i++) {
            int r = scanner.nextInt();
            String s = scanner.next();
            String ans = "";
            for (int j = 0; j < s.length(); j++) {
                ans += Character.toString(s.charAt(j)).repeat(r);
            }
            System.out.println(ans);
        }
    }
}
