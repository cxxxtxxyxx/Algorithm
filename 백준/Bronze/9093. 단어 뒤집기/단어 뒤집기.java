import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int opCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < opCount; i++) {
            String str = br.readLine();
            String[] strList = str.split(" ");
            for (int j = 0; j < strList.length; j++) {
                String reversed = new StringBuilder(strList[j]).reverse().toString();
                System.out.print(reversed + " ");
            }
            System.out.println();
        }
    }
}
