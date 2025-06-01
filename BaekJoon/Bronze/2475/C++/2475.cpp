// no.2475: 검증수 (B5)

#include <cstdio>
using namespace std;

int main() {
    int a, b, c, d, e;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    printf("%d\n", (a*a+b*b+c*c+d*d+e*e)%10);
    return 0;
}