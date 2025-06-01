// no.2630: 색종이 만들기 (S2)

#include <cstdio>
#include <vector>
#define WHITE 0
#define BLUE 1
using namespace std;

int count(vector<vector<int>>&, int, int, int, int, int);
bool filled(vector<vector<int>>&, int, int, int, int, int);

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> paper(n, vector<int>(n, 0));
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            scanf("%d", &paper[i][j]);
        }
    }
    printf("%d\n", count(paper, 0, 0, n-1, n-1, WHITE));
    printf("%d\n", count(paper, 0, 0, n-1, n-1, BLUE));
    return 0;
}

bool filled(vector<vector<int>>& paper, int r1, int c1, int r2, int c2, int color) {
    for(int r=r1; r<=r2; r++) {
        for(int c=c1; c<=c2; c++) {
            if(paper[r][c]!=color) {
                return false;
            }
        }
    }
    return true;
}

int count(vector<vector<int>>& paper, int r1, int c1, int r2, int c2, int color) {
    if(r1==r2 && c1==c2) {
        if(paper[r1][c1]==color) {
            return 1;
        }
        else {
            return 0;
        }
    }
    if(filled(paper, r1, c1, r2, c2, color)) {
        return 1;
    } else {
        int ret = 0;
        ret += count(paper, r1, c1, (r1+r2)/2, (c1+c2)/2, color);
        ret += count(paper, (r1+r2)/2+1, c1, r2, (c1+c2)/2, color);
        ret += count(paper, r1, (c1+c2)/2+1, (r1+r2)/2, c2, color);
        ret += count(paper, (r1+r2)/2+1, (c1+c2)/2+1, r2, c2, color);
        return ret;
    }
}