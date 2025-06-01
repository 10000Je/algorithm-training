// no.15964: 이상한 기호 (B5)

#include <cstdio>
using namespace std;

int main() {
    long long a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", (a+b)*(a-b));
    return 0;
}