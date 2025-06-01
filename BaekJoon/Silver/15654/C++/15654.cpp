// no.15654: N과 M (5) (S3)

#include <cstdio>
#include <vector>
#include <algorithm>
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
    for(int num : nums) {
        dfs(num, 1, {}, ret);
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
    for(int num : nums) {
        if(find(tmp.begin(), tmp.end(), num) != tmp.end())
            continue;
        dfs(num, depth+1, tmp, ret);
    }
}