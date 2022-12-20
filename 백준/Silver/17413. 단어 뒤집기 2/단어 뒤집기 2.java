import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();

        StringBuilder sb = new StringBuilder();
        String[] splitedLine = line.split("");
        Stack<String> stack = new Stack<String>();
        boolean flag = false;
        for(String str : splitedLine) {
            if (str.equals("<")) {
                while (!stack.isEmpty()) {
                    sb.append(stack.pop());
                }
                flag = true;
            }
            else if (str.equals(">")) {
                flag = false;
                sb.append(str);
                continue;
            }

            if (flag == true) {
                sb.append(str);
            }
            else if (flag == false) {
                if (str.equals(" ")) {
                    while (!stack.isEmpty()) {
                        sb.append(stack.pop());
                    }
                    sb.append(str);
                    continue;
                } else {
                    stack.push(str);
                }
            }
        }

        while(!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        System.out.println(sb.toString());

    }
}
