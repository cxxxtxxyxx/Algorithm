import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = 1;
        int remainBird = N;
        int sum = 0;
        int res = 0;

        while (true) {
            if (remainBird < K) {
                K = 1;
            }
            sum += K;
            remainBird -= K;
            res++;
            K++;

            if (sum >= N) {
                System.out.println(res);
                break;
            }
        }

    }
}
