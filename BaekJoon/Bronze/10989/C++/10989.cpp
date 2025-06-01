// no.10989: 수 정렬하기 3 (B1)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int nums[10001] = {0};
    for(int i=0; i<n; i++) {
        int num;
        scanf("%d", &num);
        nums[num]++;
    }
    for(int i=1; i<=10000; i++) {
        if(nums[i] > 0) {
            for(int j=0; j<nums[i]; j++) {
                printf("%d\n", i);
            }
        }
    }
    return 0;
}