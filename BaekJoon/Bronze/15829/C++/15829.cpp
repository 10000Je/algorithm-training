// no.15829: Hashing (B2)

#include <cstdio>
using namespace std;

int r=31, m=1234567891;

long long power(int x, int y);

int main() {
    int l;
    char str[100];
    scanf("%d", &l);
    getchar();
    fgets(str, 100, stdin);
    long long result = 0;
    for(int i=0; i<l; i++) {
        result += (str[i]-'a'+1)*power(r, i)%m; // 산술변환에 유의할것
    }
    result %= m;
    printf("%lld\n", result);
    return 0;
}

long long power(int x, int y) {
    long long result = 1;
    for(int i=0; i<y; i++) {
        result *= x;
        result %= m;
    }
    return result;
}

