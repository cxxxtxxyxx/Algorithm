
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        for (int i = 0; i < N; i++) {
            String test = scanner.next().strip();

            int length = test.length();

            int count = 0;
            int sum = 0;
            for (int j = 0; j < length; j++) {

                if (test.charAt(j) == 'O') {
                    count += 1;
                    sum += count;
                } else {
                    count = 0;

                }
            }

            System.out.println(sum);

        }

    }
}
