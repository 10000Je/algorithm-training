// no.2828: 사과 담기 게임

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt();
        int J = sc.nextInt();
        
        int left = 0, right = M - 1;

        int count = 0;
        for(int i=0; i<J; i++) {
            int apple = sc.nextInt() - 1;
            if(apple < left) {
                int move = left - apple;
                count += move;
                left -= move;
                right -= move;
            }
            else if(apple > right) {
                int move = apple - right;
                count += move;
                right += move;
                left += move;
            }
            else {
                // does not move
            }
        }

        System.out.println(count);
    }

}
