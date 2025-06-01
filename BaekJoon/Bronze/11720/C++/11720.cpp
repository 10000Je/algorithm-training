// no.11720: 숫자의 합 (B4)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    getchar();
    char nums[101];
    fgets(nums, 101, stdin);
    int result = 0;
    for(int i=0; i<n; i++) {
        result += nums[i]-'0';
    }
    printf("%d\n", result);
    return 0;
}