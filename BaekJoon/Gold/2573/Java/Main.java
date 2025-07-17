// no.2573: 빙산

import java.util.*;
import java.io.*;

class Pair {
    int r, c;
    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

enum State {
    SPLIT, NOT_SPLIT, MELT
}

public class Main {
    
    static int N, M;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[][] sea = new int[N][M];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                sea[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int count = 0;
        while(check(sea) == State.NOT_SPLIT) {
            sea = melt(sea);
            count++;
        }
        
        if(check(sea) == State.MELT) {
            System.out.println(0);
        }
        else {
            System.out.println(count);
        }
    }

    static int[][] melt(int[][] sea) {
        int[][] result = new int[N][M];
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(sea[i][j] == 0) {
                    continue;
                }
                Pair[] nodes = new Pair[] {
                    new Pair(i-1, j), new Pair(i+1, j),
                    new Pair(i, j-1), new Pair(i, j+1)
                };
                int count = 0;
                for(Pair node : nodes) {
                    if(sea[node.r][node.c] == 0) {
                        count++;
                    }
                }
                result[i][j] = Math.max(0, sea[i][j] - count); // 초과해서 녹지 않게
            }
        }
        return result;
    }

    // 둘로 분리되었으면 SPLIT, 분리가 아직 안됬으면 NOT_SPLIT, 분리가 안되고 다 녹았다면 MELT
    static State check(int[][] sea) {
        boolean[][] visit = new boolean[N][M];

        int count = 0;
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(sea[i][j] != 0 && !visit[i][j]) {
                    dfs(new Pair(i, j), sea, visit);
                    count++;
                }
            }
        }

        if(count == 1) {
            return State.NOT_SPLIT;
        }
        else if(count == 0) {
            return State.MELT;
        }
        else {
            return State.SPLIT;
        }
    }

    static void dfs(Pair loc, int[][] sea, boolean[][] visit) {
        visit[loc.r][loc.c] = true;
        
        Pair[] nodes = new Pair[] {
            new Pair(loc.r-1, loc.c), new Pair(loc.r+1, loc.c),
            new Pair(loc.r, loc.c-1), new Pair(loc.r, loc.c+1)
        };
        for(Pair node : nodes) {
            if(sea[node.r][node.c] == 0) {
                continue;
            }
            if(visit[node.r][node.c]) {
                continue;
            }
            dfs(node, sea, visit);
        }
    }

}
