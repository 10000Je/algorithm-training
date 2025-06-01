// no.15663: N과 M (9) (S2)

#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

void dfs(int, int, int, vector<int>, vector<vector<int>>&);

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
    dfs(-1, 0, 0, {}, ret);
    for(vector<int>& arr : ret) {
        for(int num : arr) {
            printf("%d ", num);
        }
        printf("\n");
    }
    return 0;
}

void dfs(int idx, int depth, int check, vector<int> tmp, vector<vector<int>>& ret) {
    if(idx != -1) {
        tmp.push_back(nums[idx]);
        check = check | (1<<idx);
    }
    if(depth == m) {
        ret.push_back(tmp);
        return;
    }
    vector<int> selected;
    for(int i=0; i<n; i++) {
        if((1<<i) & check)
            continue;
        if(find(selected.begin(), selected.end(), nums[i]) != selected.end())
            continue;
        selected.push_back(nums[i]);
        dfs(i, depth+1, check, tmp, ret);
    }
}