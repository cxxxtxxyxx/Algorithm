import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        int rest = K;
        int[] arr = new int[N];
        int res = 0;

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            res += rest / arr[i];
            rest -= arr[i] * (rest/ arr[i]);
        }
        System.out.println(res);
    }
}

