import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<Integer>();
        int top = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int element = Integer.parseInt(br.readLine());
            try {
                if (element > top) {
                    for (int j = top + 1; j <= element; j++) {
                        stack.push(j);
                        sb.append("+\n");
                    }
                    top = element;
                    stack.pop();
                    sb.append("-\n");
                } else {
                    while (stack.peek() != element) {
                        stack.pop();
                        sb.append("-\n");
                    }
                    stack.pop();
                    sb.append("-\n");
                }
            } catch (EmptyStackException e) {
                System.out.println("NO");
                return;
            }

        }
        System.out.println(sb.toString());
    }
}
