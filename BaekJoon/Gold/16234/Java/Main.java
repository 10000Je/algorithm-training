// no.16234: 인구 이동

import java.util.*;
import java.io.*;

class Pair {
    int r, c;

    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }

    boolean equals(Pair other) {
        return this.r == other.r && this.c == other.c;
    }
}

public class Main {
    
    static int N, L, R;
    static Pair[][] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        parent = new Pair[N][N];

        int[][] A = new int[N][N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int count = 0;
        while(true) {
            int[][] newA = move(A);
            if(check(A, newA)) {
                break;
            }
            A = newA;
            count++;
        }
        System.out.println(count);
    }

    static int[][] move(int[][] A) {
        // init
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                parent[i][j] = new Pair(i, j);
            }
        }

        // open
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                Pair[] nodes = new Pair[] {
                    new Pair(i-1, j), new Pair(i+1, j),
                    new Pair(i, j-1), new Pair(i, j+1)
                };
                for(Pair node : nodes) {
                    if(node.r < 0 || node.r >= N || node.c < 0 || node.c >= N) {
                        continue;
                    }
                    if(L <= Math.abs(A[i][j] - A[node.r][node.c]) 
                    && Math.abs(A[i][j] - A[node.r][node.c]) <= R) {
                        union(new Pair(i, j), node);
                    }
                }
            }
        }

        int[][] total = new int[N][N]; // root 에 합계 진행, root 가 아니면 0
        int[][] count = new int[N][N]; // 분리 집합의 크기, root 가 아니면 0

        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                Pair root = find(new Pair(i, j));
                total[root.r][root.c] += A[i][j];
                count[root.r][root.c]++;
            }
        }

        int[][] result = new int[N][N];
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                Pair root = find(new Pair(i, j));
                result[i][j] = total[root.r][root.c] / count[root.r][root.c];
            }
        }
        return result;
    }

    // 두 배열의 상태가 다르면 false, 같으면 true
    static boolean check(int[][] A, int[][] newA) {
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(A[i][j] != newA[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    static Pair find(Pair x) {
        int r = x.r, c = x.c;
        if(!parent[r][c].equals(x)) {
            parent[r][c] = find(parent[r][c]);
        }
        return parent[r][c];
    }

    // a를 b에 붙이기
    static void union(Pair a, Pair b) {
        Pair rootA = find(a);
        Pair rootB = find(b);
        parent[rootA.r][rootA.c] = rootB;
    }

}
