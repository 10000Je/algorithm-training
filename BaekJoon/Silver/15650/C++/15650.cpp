// no.15650: N과 M (2) (S3)

#include <cstdio>
#include <vector>
#include <algorithm>
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
    for(int i=num+1; i<=n; i++) {
        if(find(tmp.begin(), tmp.end(), i) != tmp.end())
            continue;
        dfs(i, depth+1, tmp, ret);
    }
}