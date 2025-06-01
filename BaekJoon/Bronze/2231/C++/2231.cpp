// no.2231: 분해합 (B2)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for(int i=1; i<n; i++) {
        char str[100];
        sprintf(str, "%d", i);
        int idx = 0, sum = i;
        while(str[idx]) {
            sum += str[idx]-'0';
            idx++;
        }
        if(sum == n) {
            printf("%d\n", i);
            return 0;
        }
    }
    printf("0\n");
    return 0;
}