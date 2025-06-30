import java.util.*;
import java.io.*;

class Main {

    static int[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        List<int[]> black = new ArrayList<>();
        List<int[]> white = new ArrayList<>();
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(board[i][j] == 0) {
                    continue;
                }
                if((i + j) % 2 == 0) {
                    white.add(new int[] { i, j });
                }   
                else {
                    black.add(new int[] { i, j });
                }
            }
        }

        System.out.println(dfs(0, 0L, black) + dfs(0, 0L, white));
    }

    // depth = 현재 탐색하는 칸, placed = 놓은 칸들(비트마스킹), arr = 놓을 수 있는 칸들의 위치
    static int dfs(int depth, long placed, List<int[]> arr) {
        int n = arr.size();
        if(depth == n) {
            int count = 0;
            for(int i=0; i<n; i++) {
                if((placed & (1L << i)) > 0) {
                    count++;
                }
            }
            return count;
        }
        int off = dfs(depth + 1, placed, arr);
        int on = check(depth, placed, arr) ? -1 : dfs(depth + 1, placed | (1L << depth), arr);
        return Math.max(on, off);
    }

    // true -> 서로 공격함
    static boolean check(int d, long placed, List<int[]> arr) {
        for(int i=0; i<d; i++) {
            if((placed & (1L << i)) == 0) {
                continue;
            }
            int dr = arr.get(d)[0], dc = arr.get(d)[1];
            int r = arr.get(i)[0], c = arr.get(i)[1];
            if(Math.abs(dr-r) == Math.abs(dc-c)) {
                return true;
            }
        }
        return false;
    }

}