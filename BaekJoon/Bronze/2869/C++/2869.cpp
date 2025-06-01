// no.2869: 달팽이는 올라가고 싶다 (B1)

#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    int a, b, v;
    scanf("%d %d %d", &a, &b, &v);
    printf("%d\n", int(ceil(double((v-a))/(a-b)))+1);
    return 0;
}