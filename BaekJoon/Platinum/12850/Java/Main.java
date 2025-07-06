// no.12850: 본대 산책 2

import java.util.*;
import java.io.*;

class Main {

    static int[][] graph = new int[][] {
        // 정 전 미 신 진 한 학 형
        {0, 1, 1, 0, 0, 0, 0, 0}, // 정보 과학관
        {1, 0, 1, 1, 0, 0, 0, 0}, // 전산관
        {1, 1, 0, 1, 0, 1, 0, 0}, // 미래관
        {0, 1, 1, 0, 1, 1, 0, 0}, // 신양관
        {0, 0, 0, 1, 0, 1, 1, 0}, // 진리관
        {0, 0, 1, 1, 1, 0, 0, 1}, // 한경직기념관
        {0, 0, 0, 0, 1, 0, 0, 1}, // 학생회관
        {0, 0, 0, 0, 0, 1, 1, 0}, // 형남공학관
    };

    static final long R = 1_000_000_007L;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int d = Integer.parseInt(br.readLine());
        int[][] result = power(graph, d);
        System.out.println(result[0][0]);
    }

    static int[][] power(int[][] a, int n) {
        if(n == 1) {
            return a; // 변경이 없으므로 그대로 반환해도 무방
        }
        int[][] temp = power(a, n/2);
        if(n % 2 == 0) {
            return cross(temp, temp);
        }
        else {
            return cross(cross(temp, temp), a);
        }

    } 

    static int[][] cross(int[][] a, int[][] b) {
        int[][] result = new int[a.length][b[0].length];

        for(int i=0; i<a.length; i++) {
            for(int j=0; j<b[0].length; j++) {
                result[i][j] = 0;
                for(int k=0; k<b.length; k++) {
                    result[i][j] += ((long)a[i][k] * b[k][j] % R);
                    result[i][j] %= R;
                }
            }
        }

        return result;
    }

}