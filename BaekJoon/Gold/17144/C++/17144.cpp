// no.17144: 미세먼지 안녕! (G4)

#include <cstdio>
#include <vector>
using namespace std;

int r, c;
int p;
int room[50][50];

void spread();
void purify();

int main() {
    int t;
    scanf("%d %d %d", &r, &c, &t);
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            scanf("%d", &room[i][j]);
            if(room[i][j] == -1) {
                p = i;
            }
        }
    }
    
    for(int i=0; i<t; i++) {
        spread();
        purify();
    }
    int ret = 0;
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            if(room[i][j] > 0) {
                ret += room[i][j];
            }
        }
    }
    printf("%d\n", ret);
    return 0;
}

void spread() {
    vector<pair<int, int>> dusts;
    int dust[50][50];
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            if(room[i][j] > 0) {
                dust[i][j] = room[i][j];
            }
            else {
                dust[i][j] = -1;
            }
        }
    }
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            if(dust[i][j] == -1) {
                continue;
            }
            vector<pair<int, int>> nodes = {
                make_pair(i-1, j), make_pair(i+1, j), make_pair(i, j-1), make_pair(i, j+1)
            };
            int cnt = 0;
            for(pair<int, int> node : nodes) {
                int nr = node.first, nc = node.second;
                if(nr < 0 || nr >= r || nc < 0 || nc >= c) {
                    continue;
                }
                if(room[nr][nc] == -1) {
                    continue;
                }
                room[nr][nc] += (dust[i][j]/5);
                cnt++;
            }
            room[i][j] = room[i][j] - (dust[i][j]/5) * cnt;
        }
    }
}

void purify() {
    // upstream
    for(int i=p-2; i>0; i--) {
        room[i][0] = room[i-1][0];
    }
    for(int i=0; i<c-1; i++) {
        room[0][i] = room[0][i+1];
    }
    for(int i=0; i<p-1; i++) {
        room[i][c-1] = room[i+1][c-1];
    }
    for(int i=c-1; i>1; i--) {
        room[p-1][i] = room[p-1][i-1];
    }
    room[p-1][1] = 0;

    // downstream
    for(int i=p+1; i<r-1; i++) {
        room[i][0] = room[i+1][0];
    }
    for(int i=0; i<c-1; i++) {
        room[r-1][i] = room[r-1][i+1];
    }
    for(int i=r-1; i>p; i--) {
        room[i][c-1] = room[i-1][c-1];
    }
    for(int i=c-1; i>1; i--) {
        room[p][i] = room[p][i-1];
    }
    room[p][1] = 0;
}
