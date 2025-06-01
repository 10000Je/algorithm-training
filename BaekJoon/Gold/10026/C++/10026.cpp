// no.10026: 적록색약 (G5)

#include <cstdio>
#include <vector>
using namespace std;

void dfs(vector<vector<char>>&, pair<int, int>, bool);

int n;

int main() {
    scanf("%d", &n);
    vector<vector<char>> paint_1(n, vector<char>(n, 0));
    vector<vector<char>> paint_2(n, vector<char>(n, 0));
    for(int i=0; i<n; i++) {
        char str[101];
        scanf("%s", str);
        for(int j=0; str[j]!=0; j++) {
            paint_1[i][j] = str[j];
            paint_2[i][j] = str[j];
        }
    }
    int cnt_1 = 0;
    int cnt_2 = 0;
    for(int r=0; r<n; r++) {
        for(int c=0; c<n; c++) {
            if(paint_1[r][c] != 0) {
                dfs(paint_1, make_pair(r, c), false);
                cnt_1++;
            }
            if(paint_2[r][c] != 0) {
                dfs(paint_2, make_pair(r, c), true);
                cnt_2++;
            }
        }
    }
    printf("%d %d\n", cnt_1, cnt_2);
    return 0;
}

void dfs(vector<vector<char>>& paint, pair<int, int> root, bool blind) {
    int r=root.first, c=root.second;
    char color = paint[r][c];
    paint[r][c] = 0;
    vector<pair<int, int>> nodes = {
        make_pair(r-1, c), make_pair(r+1, c), make_pair(r, c-1), make_pair(r, c+1)
    };
    for(pair<int, int> node : nodes) {
        int nr=node.first, nc=node.second;
        if(nr<0 || nr>=n)
            continue;
        if(nc<0 || nc>=n)
            continue;
        if(paint[nr][nc] == 0)
            continue;
        if(blind && (color=='R' || color=='G')) {
            if(paint[nr][nc]=='R' || paint[nr][nc]=='G')
                dfs(paint, node, blind);
        }
        else {
            if(paint[nr][nc]==color)
                dfs(paint, node, blind);
        }
    } 
}