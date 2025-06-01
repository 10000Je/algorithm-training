// no.30802: 웰컴 키트 (B3)

#include <cstdio>
using namespace std;

int main() {
    int n;
    int s, m, l, xl, xxl, xxxl;
    int t, p;
    scanf("%d", &n);
    scanf("%d %d %d %d %d %d", &s, &m, &l, &xl, &xxl, &xxxl);
    scanf("%d %d", &t, &p);

    int ret1 = 0;
    ret1 += s%t ? s/t+1 : s/t;
    ret1 += m%t ? m/t+1 : m/t;
    ret1 += l%t ? l/t+1 : l/t;
    ret1 += xl%t ? xl/t+1 : xl/t;
    ret1 += xxl%t ? xxl/t+1 : xxl/t;
    ret1 += xxxl%t ? xxxl/t+1 : xxxl/t;
    printf("%d\n", ret1);
    printf("%d %d\n", n/p, n%p);
    return 0;
}