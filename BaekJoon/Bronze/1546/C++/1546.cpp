// no.1546: 평균 (B1)

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    getchar();
    char str[10000];
    fgets(str, 10000, stdin);
    str[strlen(str)-1] = 0;

    vector<int> nums;
    char* result = strtok(str, " ");
    while(result != NULL) {
        nums.push_back(atoi(result));
        result = strtok(NULL, " ");
    }
    double m = *max_element(nums.begin(), nums.end());
    double total = 0;
    for(int num : nums) {
        total += num/m*100;
    }
    printf("%lf\n", total/n);
    return 0;
}