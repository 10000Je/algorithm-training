// no.17143: 낚시왕

import java.util.*;
import java.io.*;

class Shark {
    int s, d, z;
    Shark(int s, int d, int z) {
        this.s = s;
        this.d = d;
        this.z = z;
    }
}

class Main {

    private static final int UP = 1;
    private static final int DOWN = 2;
    private static final int RIGHT = 3;
    private static final int LEFT = 4;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Shark[][] board = new Shark[R][C];
        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            board[r][c] = new Shark(s, d, z);
        }

        int total = 0;
        for(int i=0; i<C; i++) {
            int loc = find(i, board);
            if(loc != -1) {
                total += board[loc][i].z;
                board[loc][i] = null;
            }
            board = move(board);
        }
        System.out.println(total);
    }

    // find max size fish (return index)
    static int find(int c, Shark[][] board) {
        int R = board.length;
        for(int i=0; i<R; i++) {
            if(board[i][c] == null) {
                continue;
            }
            return i;
        }
        return -1;
    }

    static Shark[][] move(Shark[][] board) {
        int R = board.length;
        int C = board[0].length;
        Shark[][] result = new Shark[R][C];

        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if(board[i][j] == null) {
                    continue;
                }
                int s = board[i][j].s;
                int d = board[i][j].d;
                int z = board[i][j].z;
                if(d == UP) {
                    int[] ret = up(i, s, R);
                    int new_r = ret[0];
                    int new_d = ret[1];
                    if(result[new_r][j] == null || z > result[new_r][j].z) {
                        result[new_r][j] = new Shark(s, new_d, z);
                    }
                }
                if(d == DOWN) {
                    int[] ret = down(i, s, R);
                    int new_r = ret[0];
                    int new_d = ret[1];
                    if(result[new_r][j] == null || z > result[new_r][j].z) {
                        result[new_r][j] = new Shark(s, new_d, z);
                    }
                }
                if(d == LEFT) {
                    int[] ret = left(j, s, C);
                    int new_c = ret[0];
                    int new_d = ret[1];
                    if(result[i][new_c] == null || z > result[i][new_c].z) {
                        result[i][new_c] = new Shark(s, new_d, z);
                    }
                }
                if(d == RIGHT) {
                    int[] ret = right(j, s, C);
                    int new_c = ret[0];
                    int new_d = ret[1];
                    if(result[i][new_c] == null || z > result[i][new_c].z) {
                        result[i][new_c] = new Shark(s, new_d, z);
                    }
                }
            }
        }
        return result;
    }

    // arr[0]: new_r, arr[1]: new_d
    static int[] up(int r, int s, int R) {
        int p = s % (2*(R-1));
        if(p <= r) {
            return new int[] { r-p, UP };
        }
        p -= r;
        if(p < R) {
            return new int[] { p, DOWN };
        }
        p -= (R-1);
        return new int[] { (R-1)-p, UP };
    }

    static int[] down(int r, int s, int R) {
        int p = s % (2*(R-1));
        if(p < R-r) {
            return new int[] { r+p, DOWN };
        }
        p -= (R-1-r);
        if(p < R) {
            return new int[] { R-1-p, UP };
        }
        p -= (R-1);
        return new int[] { p, DOWN };
    }

    static int[] left(int c, int s, int C) {
        int p = s % (2*(C-1));
        if(p <= c) {
            return new int[] { c-p, LEFT };
        }
        p -= c;
        if(p < C) {
            return new int[] { p, RIGHT };
        }
        p -= (C-1);
        return new int[] { (C-1)-p, LEFT };
    }

    static int[] right(int c, int s, int C) {
        int p = s % (2*(C-1));
        if(p < C-c) {
            return new int[] { c+p, RIGHT };
        }
        p -= (C-1-c);
        if(p < C) {
            return new int[] { C-1-p, LEFT };
        }
        p -= (C-1);
        return new int[] { p, RIGHT };
    }

}