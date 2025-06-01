// no.2448: 별 찍기 - 11 (G4)

#include <cstdio>
#include <vector>
using namespace std;

void dnc(int, int, int);
vector<vector<char>> star;

int main() {
    int n;
    scanf("%d", &n);
    star.assign(n, vector<char>(2*n, ' '));
    dnc(0, n-1, n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<2*n; j++) {
            printf("%c", star[i][j]);
        }
        printf("\n");
    }
    return 0;
}

void dnc(int r, int c, int n) {
    if(n == 3) {
        star[r][c] = '*';
        star[r+1][c-1] = '*';
        star[r+1][c+1] = '*';
        for(int i=c-2; i<=c+2; i++)
            star[r+2][i] = '*';
        return;
    }
    dnc(r, c, n/2);
    dnc(r+n/2, c-n/2, n/2);
    dnc(r+n/2, c+n/2, n/2);
}