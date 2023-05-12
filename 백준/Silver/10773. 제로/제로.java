import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < K; i++) {
            int nextNumber = Integer.parseInt(br.readLine());
            if (nextNumber != 0) {
                stack.push(nextNumber);
                continue;
            }

            stack.pop();
        }

        System.out.println(
                stack.stream()
                        .mapToInt(Integer::intValue)
                        .sum()
        );
    }
}
