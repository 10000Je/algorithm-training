// no.15683: 감시

import java.util.*;

enum Dir {
    UP, DOWN, LEFT, RIGHT
}

class CCTV {
    Dir dir = Dir.UP;
    int r, c;

    CCTV(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {

    static final int ONE = 1;
    static final int TWO = 2;
    static final int THREE = 3;
    static final int FOUR = 4;
    static final int FIVE = 5;

    static final int BLANK = 0;
    static final int WALL = 6;

    static int N, M;
    static int[][] room;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        room = new int[N][M];
        List<CCTV> cctvs = new ArrayList<>();
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                room[i][j] = sc.nextInt();
                if(ONE <= room[i][j] && room[i][j] <= FIVE) {
                    cctvs.add(new CCTV(i, j));
                }
            }
        }
        System.out.println(dfs(0, cctvs));
    }

    // depth = 현재 방향을 정하는 CCTV의 인덱스
    static int dfs(int depth, List<CCTV> cctvs) {
        if(depth == cctvs.size()) {
            return count(cctvs);
        }
        int ret = 64;
        for(Dir dir : Dir.values()) {
            cctvs.get(depth).dir = dir; // 방향을 갱신 후 백트래킹
            ret = Math.min(dfs(depth + 1, cctvs), ret);
        }
        return ret;
    }

    // 사각지대를 카운트하는 함수
    static int count(List<CCTV> cctvs) {
        boolean[][] check = new boolean[N][M];
        for(CCTV cctv : cctvs) {
            switch(room[cctv.r][cctv.c]) {
                case ONE:
                    one(cctv, check);
                    break;
                case TWO:
                    two(cctv, check);
                    break;
                case THREE:
                    three(cctv, check);
                    break;
                case FOUR:
                    four(cctv, check);
                    break;
                case FIVE:
                    five(cctv, check);
                    break;
            }
        }

        int count = 0;
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(room[i][j] == BLANK && !check[i][j]) {
                    count++;
                }
            }
        }
        return count;
    }

    // 1번 타입 CCTV로 볼 수 있는 영역 표시
    static void one(CCTV cctv, boolean[][] check) {
        switch(cctv.dir) {
            case UP:
                up(cctv, check);
                break;
            case DOWN:
                down(cctv, check);
                break;
            case LEFT:
                left(cctv, check);
                break;
            case RIGHT:
                right(cctv, check);
                break;
        }
    }

    // 2번 타입 CCTV로 볼 수 있는 영역 표시
    static void two(CCTV cctv, boolean[][] check) {
        switch(cctv.dir) {
            case UP:
            case DOWN:
                down(cctv, check);
                up(cctv, check);
                break;
            case LEFT:
            case RIGHT:
                left(cctv, check);
                right(cctv, check);
                break;
        }
    }

    // 3번 타입 CCTV로 볼 수 있는 영역 표시
    static void three(CCTV cctv, boolean[][] check) {
        switch(cctv.dir) {
            case UP:
                up(cctv, check);
                left(cctv, check);
                break;
            case DOWN:
                down(cctv, check);
                right(cctv, check);
                break;
            case LEFT:
                left(cctv, check);
                down(cctv, check);
                break;
            case RIGHT:
                right(cctv, check);
                up(cctv, check);
                break;
        }
    }

    // 4번 타입 CCTV로 볼 수 있는 최대 영역
    static void four(CCTV cctv, boolean[][] check) {
        switch(cctv.dir) {
            case UP:
                up(cctv, check);
                left(cctv, check);
                down(cctv, check);
                break;
            case DOWN:
                down(cctv, check);
                right(cctv, check);
                up(cctv, check);
                break;
            case LEFT:
                left(cctv, check);
                down(cctv, check);
                right(cctv, check);
                break;
            case RIGHT:
                right(cctv, check);
                up(cctv, check);
                left(cctv, check);
                break;
        }
    }

    // 5번 타입 CCTV로 볼 수 있는 최대 영역
    static void five(CCTV cctv, boolean[][] check) {
        up(cctv, check);
        left(cctv, check);
        down(cctv, check);
        right(cctv, check);
    }

    // 해당 칸을 기준으로 위쪽으로 감시할 수 있는 영역을 표시함
    static void up (CCTV cctv, boolean[][] check) {
        int r = cctv.r, c = cctv.c;
        for(int i = r - 1; i >= 0 && room[i][c] != WALL; i--) {
            if(room[i][c] == BLANK) {
                check[i][c] = true;
            }
        }
    }

    // 해당 칸을 기준으로 아래쪽으로 감시할 수 있는 영역을 표시함
    static void down(CCTV cctv, boolean[][] check) {
        int r = cctv.r, c = cctv.c;
        for(int i = r + 1; i < N && room[i][c] != WALL; i++) {
            if(room[i][c] == BLANK) {
                check[i][c] = true;
            }
        }
    }

    // 해당 칸을 기준으로 왼쪽으로 감시할 수 있는 영역을 표시함
    static void left(CCTV cctv, boolean[][] check) {
        int r = cctv.r, c = cctv.c;
        for(int i = c - 1; i >= 0 && room[r][i] != WALL; i--) {
            if(room[r][i] == BLANK) {
                check[r][i] = true;
            }
        }
    }

    // 해당 칸을 기준으로 오른쪽으로 감시할 수 있는 영역을 표시함
    static void right(CCTV cctv, boolean[][] check) {
        int r = cctv.r, c = cctv.c;
        for(int i = c + 1; i < M && room[r][i] != WALL; i++) {
            if(room[r][i] == BLANK) {
                check[r][i] = true;
            }
        }
    }

}
