// no.10872: 팩토리얼 (B3)

#include <cstdio>
using namespace std;

int fact(int n);

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fact(n));
    return 0;
}

int fact(int n) {
    if(n==0)
        return 1;
    return n*fact(n-1);
}