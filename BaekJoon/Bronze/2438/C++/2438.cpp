// no.2438: 별 찍기 - 1 (B5)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        for(int j=0; j<i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}