// no.1629: 곱셈 (S1)

#include <cstdio>
using namespace std;

typedef long long int64;
int64 power(int64 a, int64 b);
int64 c;

int main() {
    int64 a, b;
    scanf("%lld %lld %lld", &a, &b, &c);
    printf("%lld\n", power(a, b));
    return 0;
}

int64 power(int64 a, int64 b) {
    if(b == 0)
        return 1;
    int64 temp = power(a, b/2);
    if(b%2 == 0)
        return (temp*temp)%c;
    else
        return (((temp*temp)%c)*a)%c;
}
