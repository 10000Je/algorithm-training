import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] board = new int[n][n];
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(dfs(0, board));
    }

    static int dfs(int depth, int[][] board)
    {
        int result = 0;
        if(depth == 5) {
            for(int[] arr : board) {
                for(int num : arr) {
                    result = Math.max(result, num);
                }
            }
            return result;
        }
        result = Math.max(result, dfs(depth+1, up(board)));
        result = Math.max(result, dfs(depth+1, down(board)));
        result = Math.max(result, dfs(depth+1, left(board)));
        result = Math.max(result, dfs(depth+1, right(board)));
        return result;
    }

    static int[][] up(int[][] board) {
        int n = board.length;
        boolean[][] check = new boolean[n][n];
        int[][] result = new int[n][n];

        // init
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                result[i][j] = board[i][j];
                check[i][j] = false;
            }
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(result[i][j] == 0)
                    continue;
                int temp = result[i][j];
                result[i][j] = 0;
                int k = i-1;
                while(k >= 0) {
                    if(result[k][j] == 0) {
                        k--;
                    }
                    else {
                        if(result[k][j] == temp && !check[k][j]) {
                            temp *= 2;
                            check[k][j] = true;
                            k--;
                        }
                        break;
                    }
                }
                result[k+1][j] = temp;
            }
        }
        return result;
    }

    static int[][] down(int[][] board) {
        int n = board.length;
        boolean[][] check = new boolean[n][n];
        int[][] result = new int[n][n];

        // init
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                result[i][j] = board[i][j];
                check[i][j] = false;
            }
        }

        for(int i=n-1; i>=0; i--) {
            for(int j=0; j<n; j++) {
                if(result[i][j] == 0)
                    continue;
                int temp = result[i][j];
                result[i][j] = 0;
                int k = i+1;
                while(k < n) {
                    if(result[k][j] == 0) {
                        k++;
                    }
                    else {
                        if(result[k][j] == temp && !check[k][j]) {
                            temp *= 2;
                            check[k][j] = true;
                            k++;
                        }
                        break;
                    }
                }
                result[k-1][j] = temp;
            }
        }
        return result;
    }

    static int[][] left(int[][] board) {
        int n = board.length;
        boolean[][] check = new boolean[n][n];
        int[][] result = new int[n][n];

        // init
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                result[i][j] = board[i][j];
                check[i][j] = false;
            }
        }

        for(int j=0; j<n; j++) {
            for(int i=0; i<n; i++) {
                if(result[i][j] == 0)
                    continue;
                int temp = result[i][j];
                result[i][j] = 0;
                int k = j-1;
                while(k >= 0) {
                    if(result[i][k] == 0) {
                        k--;
                    }
                    else {
                        if(result[i][k] == temp && !check[i][k]) {
                            temp *= 2;
                            check[i][k] = true;
                            k--;
                        }
                        break;
                    }
                }
                result[i][k+1] = temp;
            }
        }
        return result;
    }

    static int[][] right(int[][] board) {
        int n = board.length;
        boolean[][] check = new boolean[n][n];
        int[][] result = new int[n][n];

        // init
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                result[i][j] = board[i][j];
                check[i][j] = false;
            }
        }

        for(int j=n-1; j>=0; j--) {
            for(int i=0; i<n; i++) {
                if(result[i][j] == 0)
                    continue;
                int temp = result[i][j];
                result[i][j] = 0;
                int k = j+1;
                while(k < n) {
                    if(result[i][k] == 0) {
                        k++;
                    }
                    else {
                        if(result[i][k] == temp && !check[i][k]) {
                            temp *= 2;
                            check[i][k] = true;
                            k++;
                        }
                        break;
                    }
                }
                result[i][k-1] = temp;
            }
        }
        return result;
    }

}