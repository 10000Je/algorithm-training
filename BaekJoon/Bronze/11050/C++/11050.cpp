// no.11050: 이항 계수 1 (B1)

#include <cstdio>
using namespace std;

int fact(int n);

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    printf("%d\n", fact(n)/(fact(k)*fact(n-k)));
    return 0;
}

int fact(int n) {
    if(n==0)
        return 1;
    return n*fact(n-1);
}