// no.1987: 알파벳 (G4)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int, int, int, int);
vector<vector<char>> board;
int ret = 0;
int r, c;

int main() {
    scanf("%d %d", &r, &c);
    board.assign(r, vector<char>(c, 0));
    for(int i=0; i<r; i++) {
        char str[21];
        scanf("%s", str);
        getchar();
        for(int j=0; j<c; j++) {
            board[i][j] = str[j];
        }
    }
    dfs(0, 0, (1<<(board[0][0]-'A')), 1);
    printf("%d\n", ret);
    return 0;
}

void dfs(int a, int b, int visit, int depth) {
    vector<pair<int, int>> node = {
        make_pair(a-1, b), make_pair(a+1, b),
        make_pair(a, b-1), make_pair(a, b+1)
    };
    for(pair<int, int> val : node) {
        int i = val.first;
        int j = val.second;
        if(i<0 || i>=r || j<0 || j>=c)
            continue;
        if(visit & (1<<(board[i][j]-'A')))
            continue;
        dfs(i, j, visit | (1<<(board[i][j]-'A')), depth+1);
    }
    ret = max(ret, depth);
}