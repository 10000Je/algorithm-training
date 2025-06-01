// no.13172: Σ (G4)

#include <cstdio>
#define R 1'000'000'007

typedef long long int64;

int64 power(int64, int64);

int main() {
    int m;
    scanf("%d", &m);
    int64 sum = 0;
    for(int i=0; i<m; i++) {
        int64 ni, si;
        scanf("%lld %lld", &ni, &si);
        sum = (sum + ((si*power(ni, R-2))%R))%R;
    }
    printf("%lld\n", sum);
    return 0;

}

int64 power(int64 a, int64 b) {
    if(b == 0)
        return 1;
    int64 tmp = power(a, b/2);
    if(b%2 == 0) {
        return (tmp*tmp)%R;
    }
    else {
        return ((tmp*tmp%R)*a)%R;
    }
}