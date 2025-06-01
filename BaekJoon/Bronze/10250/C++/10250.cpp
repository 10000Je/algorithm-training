// no.10250: ACM 호텔 (B3)

#include <cstdio>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int h, w, n;
        scanf("%d %d %d", &h, &w, &n);
        int result = 0;
        if(n%h) {
            result += n/h+1;
            result += (n%h)*100;
        } else {
            result += n/h;
            result += h*100;
        }
        printf("%d\n", result);
    }
    return 0;
}