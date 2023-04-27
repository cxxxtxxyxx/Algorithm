import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        int blankCnt = 0;

        if (str.length() == 0) {
            System.out.println(0);
            sc.close();
            return;
        }


        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ' ') {
                
                blankCnt++;
            }
            
        }
        System.out.println(blankCnt + 1);

        sc.close();
    }    
}
