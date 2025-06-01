// no.15652: N과 M (4) (S3)

#include <cstdio>
#include <vector>
using namespace std;

void dfs(int, int, vector<int>, vector<vector<int>>&);

int n, m;

int main() {
    scanf("%d %d", &n, &m);
    vector<vector<int>> ret;
    for(int i=1; i<=n; i++) {
        dfs(i, 1, {}, ret);
    }
    for(vector<int> arr : ret) {
        for(int num : arr) {
            printf("%d ", num);
        }
        printf("\n");
    }
    return 0;
}

void dfs(int num, int depth, vector<int> tmp, vector<vector<int>>& ret) {
    tmp.push_back(num);
    if(depth == m) {
        ret.push_back(tmp);
        return;
    }
    for(int i=num; i<=n; i++) {
        dfs(i, depth+1, tmp, ret);
    }
}