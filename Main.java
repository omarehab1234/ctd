
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> arr = new  ArrayList<Integer>();
        int n = in.nextInt();
        for (int i = 2; i <= n; i++) {
            if(i%2 == 0){
                arr.add(i);
                System.out.println(i);
            }
        }
        if (arr.size() == 0) {
            System.out.println(-1);
        }
    }
}
