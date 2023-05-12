import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            Stack<Character> stack = new Stack<>();
            String inputStr = br.readLine();
            boolean flag = false;
            for (char s : inputStr.toCharArray()) {
                if (s == '(') {
                    stack.push(s);
                    continue;
                }

                if (stack.isEmpty()) {
                    System.out.println("NO");
                    flag = true;
                    break;
                }

                stack.pop();
            }

            if (!flag && stack.isEmpty()) {
                System.out.println("YES");
                continue;
            }

            if (!flag) {
                System.out.println("NO");
            }

        }
    }
}