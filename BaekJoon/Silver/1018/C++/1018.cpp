// no.1018: 체스판 다시 칠하기 (S4)

#include <cstdio>
using namespace std;

int count(char [][8]);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    char board[51][51];
    int min = 64;
    for(int i=0; i<n; i++) {
        scanf("%s", board[i]);
    }
    for(int i=0; i<=n-8; i++) {
        for(int j=0; j<=m-8; j++) {
            char cut[8][8];
            for(int k=0; k<8; k++) {
                for(int l=0; l<8; l++) {
                    cut[k][l] = board[i+k][j+l];
                }
            }
            int ret = count(cut);
            min = (ret < min) ? ret : min;
        }
    }
    printf("%d\n", min);
}

int count(char cut[][8]) {
    int point1 = 0;
    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            if((i+j)%2==0 && cut[i][j]!='W') {
                point1++;
            }
            if((i+j)%2!=0 && cut[i][j]!='B') {
                point1++;
            }
        }
    }
    int point2 = 0;
    for(int i=0; i<8; i++) {
        for(int j=0; j<8; j++) {
            if((i+j)%2==0 && cut[i][j]!='B') {
                point2++;
            }
            if((i+j)%2!=0 && cut[i][j]!='W') {
                point2++;
            }
        }
    }
    return (point1 < point2) ? point1 : point2;
}