// no.2884: 알람 시계 (B3)

#include <cstdio>
using namespace std;

int main() {
    int h, m;
    scanf("%d %d", &h, &m);
    m -= 45;
    if(m < 0) {
        h -= 1;
        m += 60;
    }
    if(h < 0) {
        h += 24;
    }
    printf("%d %d\n", h, m);
    return 0;
}