// no.19236: 청소년 상어 (G2)
/*
 * 체감 난이도: G1
 * 대표적인 구현문제에 해당하나, 물고기의 움직임을 제대로 읽지 않아서 낭패를..
 * 문제를 천천히 읽어나가는 것이 구현에서 얼마나 중요한지 다시 배울 수 있었던
 * 문제입니다.
 */

#include <cstdio>
#include <algorithm>
using namespace std;

enum {
    UP=1, LEFTUP, LEFT, LEFTDOWN, DOWN, RIGHTDOWN, RIGHT, RIGHTUP
};

struct Point {
    int r;
    int c;
};

struct Fish {
    int no;
    int dir;
};

struct Shark {
    Point loc;
    int dir;
};

void FishMove(Fish before[][4], Fish after[][4]);
void BruteForce(Fish fishState[][4], Shark shark);

int maxPoint = 0;

int main() {
    int a1, b1, a2, b2, a3, b3, a4, b4;
    Fish fishState[4][4];
    for(int i=0; i<4; i++) {
        scanf("%d %d %d %d %d %d %d %d", &a1, &b1, &a2, &b2, &a3, &b3, &a4, &b4);
        fishState[i][0] = {a1, b1};
        fishState[i][1] = {a2, b2};
        fishState[i][2] = {a3, b3};
        fishState[i][3] = {a4, b4};
    }
    Shark init = {{0, 0}, fishState[0][0].dir};
    fishState[0][0].dir = -1;
    BruteForce(fishState, init);
    printf("%d\n", maxPoint);
    return 0;
}

void FishMove(Fish before[][4], Fish after[][4]) {
    Point loc[17];
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            after[i][j] = before[i][j];
            loc[after[i][j].no] = {i, j};
        }
    }
    for(int i=1; i<=16; i++) {
        Point curLoc = loc[i];
        int dir = after[curLoc.r][curLoc.c].dir;
        if(dir == 0 || dir == -1)
            continue;
        for(int j=0; j<8; j++) {
            Point target;
            switch(dir) {
                case UP:
                    target = {curLoc.r-1, curLoc.c};
                    dir++;
                    break;
                case LEFTUP:
                    target = {curLoc.r-1, curLoc.c-1};
                    dir++;
                    break;
                case LEFT:
                    target = {curLoc.r, curLoc.c-1};
                    dir++;
                    break;
                case LEFTDOWN:
                    target = {curLoc.r+1, curLoc.c-1};
                    dir++;
                    break;
                case DOWN:
                    target = {curLoc.r+1, curLoc.c};
                    dir++;
                    break;
                case RIGHTDOWN:
                    target = {curLoc.r+1, curLoc.c+1};
                    dir++;
                    break;
                case RIGHT:
                    target = {curLoc.r, curLoc.c+1};
                    dir++;
                    break;
                case RIGHTUP:
                    target = {curLoc.r-1, curLoc.c+1};
                    dir = 1;
                    break;
            }
            if(0 <= target.r && target.r < 4 && 0 <= target.c && target.c < 4 && after[target.r][target.c].dir != -1) {
                Point tmp = loc[i];
                loc[i] = loc[after[target.r][target.c].no];
                loc[after[target.r][target.c].no] = tmp;

                Fish temp = after[curLoc.r][curLoc.c];
                after[curLoc.r][curLoc.c] = after[target.r][target.c];
                after[target.r][target.c] = temp;

                after[target.r][target.c].dir = --dir;
                if(dir == 0) {
                    after[target.r][target.c].dir = 8;
                }
                break;
            }   
        }
    }
}

void BruteForce(Fish fishState[][4], Shark shark) {
    Fish after[4][4];
    FishMove(fishState, after);
    int dir = shark.dir;
    int r = shark.loc.r, c = shark.loc.c;
    Point edible[3];
    int cnt = 0;
    switch(dir) {
        case UP:
            while(--r >= 0) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case LEFTUP:
            while(--r >= 0 && --c >= 0) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case LEFT:
            while(--c >= 0) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case LEFTDOWN:
            while(++r < 4 && --c >= 0) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case DOWN:
            while(++r < 4) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case RIGHTDOWN:
            while(++r < 4 && ++c < 4) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case RIGHT:
            while(++c < 4) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
        case RIGHTUP:
            while(--r >= 0 && ++c < 4) {
                if(after[r][c].dir != -1) {
                    edible[cnt++] = {r, c};
                }
            }
            break;
    }
    
    if(cnt == 0) {
        int point = 0;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                if(after[i][j].dir == 0 || after[i][j].dir == -1) {
                    point += after[i][j].no;
                }
            }
        }
        maxPoint = max(maxPoint, point);
        return;
    } else {
        for(int i=0; i<cnt; i++) {
            Point loc = edible[i];
            int tmp = after[loc.r][loc.c].dir;
            Fish change[4][4];
            for(int j=0; j<4; j++) {
                for(int k=0; k<4; k++) {
                    change[j][k] = after[j][k];
                }
            }
            change[loc.r][loc.c].dir = -1;
            change[shark.loc.r][shark.loc.c].dir = 0;
            BruteForce(change, {loc, after[loc.r][loc.c].dir});
        }
        return;
    }
}