// no.20144: 미아 노트

import java.util.*;
import java.io.*;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), H = sc.nextInt(), W = sc.nextInt();

        char[] result = new char[N];
        for(int i=0; i<N; i++) {
            result[i] = '?';
        }

        for(int i=0; i<H; i++) {
            String str = sc.next();
            for(int j=0; j<N*W; j++) {
                int idx = j / W;
                if(str.charAt(j) != '?') {
                    result[idx] = str.charAt(j);
                }
            }
        }
        
        for(char ch : result) {
            System.out.print(ch);
        }
        System.out.println();
    }

}
