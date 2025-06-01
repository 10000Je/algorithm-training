// no.10830: 행렬 제곱 (G4)

#include <cstdio>
#include <vector>
#define R 1000
using namespace std;

typedef long long int64;

int n;
vector<vector<int>> matrix;
vector<vector<int>> power(int64);
vector<vector<int>> multiply(vector<vector<int>>, vector<vector<int>>);

int main() {
    int64 b;
    scanf("%d %lld", &n, &b);
    matrix.assign(n, vector<int>(n, 0));
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            int num;
            scanf("%d", &num);
            matrix[i][j] = num%R;
        }
    }
    vector<vector<int>> ret = power(b);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            printf("%d ", ret[i][j]);
        }
        printf("\n");
    }
    return 0;
}

vector<vector<int>> power(int64 b) {
    if(b == 1) {
        return matrix;
    }
    vector<vector<int>> tmp = power(b/2);
    if(b%2 == 0)
        return multiply(tmp, tmp);
    else
        return multiply(multiply(tmp, tmp), matrix);
}

vector<vector<int>> multiply(vector<vector<int>> a, vector<vector<int>> b) {
    vector<vector<int>> ret(n, vector<int>(n, 0));
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            for(int k=0; k<n; k++)
                ret[i][j] = (ret[i][j] + a[i][k]*b[k][j]) % R;
    return ret;
}