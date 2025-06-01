// no.9663: N-Queen (G4)

#include <cstdio>
#include <cmath>
using namespace std;

int n;
int ret = 0;
int queen[15];
void dfs(int);

int main() {
    scanf("%d", &n);
    dfs(0);
    printf("%d\n", ret);
    return 0;
}

void dfs(int x) {
    if(x == n) {
        ret++;
        return;
    }
    for(int i=0; i<n; i++) {
        bool meet = false;
        for(int j=0; j<x; j++) {
            if(queen[j] == i) {
                meet = true;
                break;
            }
            if(abs(j-x) == abs(queen[j]-i)) {
                meet = true;
                break;
            }
        }
        if(!meet) {
            queen[x] = i;
            dfs(x+1);
            queen[x] = 0;
        }
    }
}