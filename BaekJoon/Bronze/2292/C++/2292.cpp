// no.2292: 벌집 (B2)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int dist = 0;
    int i=1;
    while(i<n) {
        dist++;
        i+=6*dist;
    }
    dist++;
    printf("%d\n", dist);
    return 0;
}