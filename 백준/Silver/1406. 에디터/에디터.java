import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String text = br.readLine();
        int N = Integer.parseInt(br.readLine());

        Stack<String> leftStr = new Stack<String>();
        leftStr.addAll(Arrays.asList(text.split("")));
        Stack<String> rightStr = new Stack<String>();

        for (int i = 0; i < N; i++) {
            String opStr[] = br.readLine().split(" ");

            switch (opStr[0]) {
                case "L":
                    if (leftStr.size() != 0)
                        rightStr.push(leftStr.pop());
                    break;
                case "D":
                    if (rightStr.size() != 0)
                        leftStr.push(rightStr.pop());
                    break;
                case "B":
                    if (leftStr.size() != 0)
                        leftStr.pop();
                    break;
                case "P":
                    leftStr.push(opStr[1]);
                    break;
                default:
                    break;
            }

        }
        while (leftStr.size() != 0) {
            rightStr.push(leftStr.pop());
        }
        while (rightStr.size() != 0) {
            sb.append(rightStr.pop());
        }

        System.out.println(sb.toString());
    }

}
