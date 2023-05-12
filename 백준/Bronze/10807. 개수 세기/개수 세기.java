import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        String[] arr = br.readLine().split(" ");

        String V = br.readLine();
        int count = 0;
        for (String a : arr) {
            if (a.equals(V)) {
                count += 1;
            }
        }


        System.out.println(count);
        
    }
}
