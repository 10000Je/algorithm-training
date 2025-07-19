// no.2890: 카약

import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken()), C = Integer.parseInt(st.nextToken());
        char[][] map = new char[R][C];
        for(int i=0; i<R; i++) {
            String str = br.readLine();
            for(int j=0; j<C; j++) {
                map[i][j] = str.charAt(j);
            }
        }
        
        int[] rank = new int[10];
        int cur = 1;
        for(int i=C-2; i>0; i--) {
            boolean isRanked = false;
            for(int j=0; j<R; j++) {
                if(map[j][i] == '.') {
                    continue; // 빈 공간
                }
                int cayak = map[j][i] - '0';
                if(rank[cayak] != 0) {
                    continue; // 이미 순위가 매겨진 카약
                }
                rank[cayak] = cur;
                isRanked = true;
            }
            if(isRanked) {
                cur++;
            }
        }

        for(int i=1; i<=9; i++) {
            System.out.println(rank[i]);
        }
    }

}