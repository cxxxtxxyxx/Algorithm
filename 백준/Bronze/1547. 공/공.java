import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int doingCount = sc.nextInt();

        int currentPosition = 1;

        for (int count = 0; count < doingCount; count++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            if (x == y) {
                System.out.println(-1);
                return;
            }

            if (x == currentPosition || y == currentPosition) {
                currentPosition = x == currentPosition ? y : x;
            }
        }

        System.out.println(currentPosition);
    }
}
