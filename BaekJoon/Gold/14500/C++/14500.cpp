// no.14500: 테트로미노 (G4)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(pair<int, int>, int, vector<pair<int, int>>, vector<vector<pair<int, int>>>&);

int main() {
    vector<vector<pair<int, int>>> ret;
    vector<pair<int, int>> tmp;
    dfs(make_pair(0, 0), 1, tmp, ret);
    ret.push_back({make_pair(0, 0), make_pair(0, 1), make_pair(0, 2), make_pair(1, 1)});
    ret.push_back({make_pair(0, 0), make_pair(0, 1), make_pair(0, 2), make_pair(-1, 1)});
    ret.push_back({make_pair(0, 0), make_pair(1, 0), make_pair(2, 0), make_pair(1, -1)});
    ret.push_back({make_pair(0, 0), make_pair(1, 0), make_pair(2, 0), make_pair(1, 1)});
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> paper(n, vector<int>(m, 0));
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            scanf("%d", &paper[i][j]);
    int max = 0;
    for(vector<pair<int, int>> block : ret) {
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                int sum = 0;
                for(int k=0; k<4; k++) {
                    int r = block[k].first;
                    int c = block[k].second;
                    if(i+r<0 || i+r>=n) {
                        sum = 0;
                        break;
                    }
                    if(j+c<0 || j+c>=m) {
                        sum = 0;
                        break;
                    }
                    sum += paper[i+r][j+c];
                }
                if(sum > max)
                    max = sum;
            }
        }
    }
    printf("%d\n", max);
    return 0;
}

void dfs(pair<int, int> loc, int depth, vector<pair<int, int>> tmp, vector<vector<pair<int, int>>>& ret) {
    tmp.push_back(loc);
    if(depth == 4) {
        ret.push_back(tmp);
        return;
    }
    vector<pair<int, int>> nodes = {
        make_pair(0, 1), make_pair(0, -1), make_pair(-1, 0), make_pair(1, 0)
    };
    for(pair<int, int> node : nodes) {
        int r = node.first;
        int c = node.second;
        if(find(tmp.begin(), tmp.end(), make_pair(loc.first+r, loc.second+c)) != tmp.end())
            continue;
        dfs(make_pair(loc.first+r, loc.second+c), depth+1, tmp, ret);
    }
    return;
}