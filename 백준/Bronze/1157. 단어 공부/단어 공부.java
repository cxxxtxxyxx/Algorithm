import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String input = sc.next().toLowerCase();

        int max = 0;
        boolean flag = false;
        String res = "";
        for (int i = 0; i < 26; i++) {
            int count = input.length() - input.replace(Character.toString('a' + i), "").length();

            if (max < count) {
                max = count;
                res = Character.toString('a' + i).toUpperCase();
                flag = false;
                continue;
            }

            if (max == count) {
                flag = true;
                continue;
            }
        }

        if (flag == true) {
            System.out.println("?");
            sc.close();

            return;
        }

        System.out.println(res);
    }
}