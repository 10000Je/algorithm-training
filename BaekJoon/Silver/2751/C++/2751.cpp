// no.2751: 수 정렬하기 2 (S5)

#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> nums;
    for(int i=0; i<n; i++) {
        int num;
        scanf("%d", &num);
        nums.push_back(num);
    }
    sort(nums.begin(), nums.end());
    for(int num : nums) {
        printf("%d\n", num);
    }
    return 0;
}