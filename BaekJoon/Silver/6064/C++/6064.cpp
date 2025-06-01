// no.6064: 카잉 달력 (S1)
/*
 * 처음에 set을 이용하여 m으로 나눈 나머지가 x이고 n으로 나눈 나머지가 y인 수를 찾으려고 했는데
 * 시간초과, set에 저장해둘 필요가 없다는 걸 깨닫고 코드 수정 -> AC
 */

#include <cstdio>
using namespace std;

int gcd(int, int);

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int m, n, x, y;
        scanf("%d %d %d %d", &m, &n, &x, &y);
        int max = m*n/gcd(m,n);
        int ret = -1;
        for(int j=y; j<=max; j+=n) {
            if(j%m == x%m) {
                ret = j;
                break;
            }
        }
        printf("%d\n", ret);
    }
    return 0;
}

int gcd(int a, int b) {
    if(b==0)
        return a;
    return gcd(b, a%b);
}

