// no.2738: 행렬 덧셈 (B3)

#include <cstdio>
#include <sstream>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    getchar();
    
    int a[100][100];
    int b[100][100];
    for(int i=0; i<n; i++) {
        char str[int(1e4)];
        fgets(str, int(1e4), stdin);
        istringstream iss(str);
        string buffer;
        int j=0;
        while(getline(iss, buffer, ' ')) {
            a[i][j++] = stoi(buffer);
        }
    }
    for(int i=0; i<n; i++) {
        char str[int(1e4)];
        fgets(str, int(1e4), stdin);
        istringstream iss(str);
        string buffer;
        int j=0;
        while(getline(iss, buffer, ' ')) {
            b[i][j++] = stoi(buffer);
        }
    }

    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            printf("%d ", a[i][j]+b[i][j]);
        }
        printf("\n");
    }
    return 0;
}