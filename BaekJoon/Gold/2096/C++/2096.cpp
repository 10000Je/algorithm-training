// no.2096: 내려가기 (G5)

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int val[100'000][3];
    for(int i=0; i<n; i++)
        for(int j=0; j<3; j++)
            scanf("%d", &val[i][j]);
    vector<int> dp_i(3, 0);
    vector<int> dp_i_1(3, 0);
    dp_i = {val[0][0], val[0][1], val[0][2]};
    for(int i=1; i<n; i++) {
        dp_i_1 = dp_i;
        dp_i[0] = max(dp_i_1[0], dp_i_1[1]) + val[i][0];
        dp_i[1] = max({dp_i_1[0], dp_i_1[1], dp_i_1[2]}) + val[i][1];
        dp_i[2] = max(dp_i_1[1], dp_i_1[2]) + val[i][2];
    }
    int ret1 = max({dp_i[0], dp_i[1], dp_i[2]});
    dp_i = {val[0][0], val[0][1], val[0][2]};
    for(int i=1; i<n; i++) {
        dp_i_1 = dp_i;
        dp_i[0] = min(dp_i_1[0], dp_i_1[1]) + val[i][0];
        dp_i[1] = min({dp_i_1[0], dp_i_1[1], dp_i_1[2]}) + val[i][1];
        dp_i[2] = min(dp_i_1[1], dp_i_1[2]) + val[i][2];
    }
    int ret2 = min({dp_i[0], dp_i[1], dp_i[2]});
    printf("%d %d\n", ret1, ret2);
    return 0;
}