import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);

        List<Integer> tmp = IntStream.rangeClosed(1, N).boxed().collect(Collectors.toList());

        List<Integer> result = new ArrayList<Integer>();
        List<Integer> nums = new ArrayList<Integer>(tmp);

        int idx = 0;
        while (result.size() != N) {
            idx = (idx + K - 1) % nums.size();
            result.add(nums.get(idx));
            nums.remove(idx);
        }

        String resultstr = result.stream().map(String::valueOf).collect(Collectors.joining(", "));

        System.out.println("<" + resultstr + ">");
    }
}
