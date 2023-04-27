import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        boolean sumFlag = false;

        int[] numArr = new int[N];

        for (int idx = 0; idx < N; idx++) {
            numArr[idx] = sc.nextInt();
        }

        if (numArr[1] - numArr[0] == numArr[2] - numArr[1]) {
            System.out.println(numArr[N - 1] + numArr[1] - numArr[0]);
        } else {
            System.out.println(numArr[N - 1] * (numArr[1] / numArr[0]));
        }
        

    }   
}
