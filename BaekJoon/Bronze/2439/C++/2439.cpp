// no.2439: 별 찍기 - 2 (B4)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        for(int j=0; j<n-i; j++) {
            printf(" ");
        }
        for(int j=0; j<i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}