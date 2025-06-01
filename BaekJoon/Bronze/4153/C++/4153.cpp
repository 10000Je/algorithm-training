// no.4153: 직각삼각형 (B3)

#include <cstdio>
using namespace std;

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    while(!(a==0 && b==0 && c==0)) {
        if(a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a) {
            printf("right\n");
        } else {
            printf("wrong\n");
        }
        scanf("%d %d %d", &a, &b, &c);
    }
    return 0;
}