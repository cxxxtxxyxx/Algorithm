import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();

        while (!str.equals("#")) {

            List<String> strList = Arrays.asList(str.split(""));

            long count = strList.stream()
            .filter(el -> "aeiouAEIOU".contains(el))
                    .count();
            
            System.out.println(count);

            str = sc.nextLine();
        }
    }
}
