// no.7568: 덩치 (S5)

#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int rank[n] = {0};
    int heights[n], weights[n];
    for(int i=0; i<n; i++) {
        int h, w;
        scanf("%d %d", &h, &w);
        heights[i] = h;
        weights[i] = w;
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(i==j)
                continue;
            if(heights[i] < heights[j] && weights[i] < weights[j])
                rank[i]++;
        }
    }
    for(int k : rank) {
        printf("%d ", k+1);
    }
    printf("\n");
    return 0;
}