// no.15666: N과 M (12) (S2)

#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

void dfs(int, int, vector<int>, vector<vector<int>>&);

int n, m;
vector<int> nums;

int main() {
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) {
        int num;
        scanf("%d", &num);
        nums.push_back(num);
    }
    sort(nums.begin(), nums.end());
    vector<vector<int>> ret;
    dfs(-1, 0, {}, ret);
    for(vector<int>& arr : ret) {
        for(int num : arr) {
            printf("%d ", num);
        }
        printf("\n");
    }
    return 0;
}

void dfs(int idx, int depth, vector<int> tmp, vector<vector<int>>& ret) {
    if(idx != -1)
        tmp.push_back(nums[idx]);
    if(depth == m) {
        ret.push_back(tmp);
        return;
    }
    vector<int> select;
    if(idx == -1)
        idx = 0;
    for(int i=idx; i<n; i++) {
        if(find(select.begin(), select.end(), nums[i]) != select.end())
            continue;
        select.push_back(nums[i]);
        dfs(i, depth+1, tmp, ret);
    }
}