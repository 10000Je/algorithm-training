// no.2609: 최대공약수와 최소공배수 (B1)

#include <cstdio>
using namespace std;

int gcd(int a, int b);

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", gcd(a, b));
    printf("%d\n", a*b/gcd(a, b));
    return 0;
}

int gcd(int a, int b) {
    if(b==0)
        return a;
    return gcd(b, a%b);
}