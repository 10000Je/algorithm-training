// no.2799: 블라인드

#include <cstdio>
#include <vector>
using namespace std;

int check(vector<vector<char>>&, int, int);

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    vector<vector<char>> apt(5*m+1, vector<char>(5*n+1, 0));
    for(int i=0; i<5*m+1; i++) {
        char str[502];
        scanf("%s", str);
        for(int j=0; j<5*n+1; j++) {
            apt[i][j] = str[j];
        }
    }
    vector<int> cnt(5, 0);
    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            int ret = check(apt, 5*i+1, 5*j+1);
            cnt[ret]++;
        }
    }
    for(int i=0; i<5; i++) {
        printf("%d ", cnt[i]);
    }
    printf("\n");
    return 0;
}

int check(vector<vector<char>>& apt, int r, int c) {
    int ret = 0;
    for(int i=0; i<5; i++) {
        if(apt[r+i][c]=='*')
            ret++;
    }
    return ret;
}