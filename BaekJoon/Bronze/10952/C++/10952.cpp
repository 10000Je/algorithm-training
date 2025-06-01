// no.10952: A+B - 5 (B5)

#include <cstdio>
using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    while(!(a==0 && b==0)) {
        printf("%d\n", a+b);
        scanf("%d %d", &a, &b);
    }
    return 0;
}