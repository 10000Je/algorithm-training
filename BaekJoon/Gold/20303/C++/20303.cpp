// no.20303: 할로윈의 양아치

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int parent[30001];

int find(int x);

void _union(int a, int b);

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n, m, k;
    cin >> n >> m >> k;
    for(int i=1; i<=n; i++)
        parent[i] = i;

    vector<int> c(n+1, 0);
    for(int i=1; i<=n; i++)
        cin >> c[i];
    
    for(int i=0; i<m; i++)
    {
        int a, b;
        cin >> a >> b;
        _union(a, b);
    }

    vector<int> temp_w(n+1, 0);
    vector<int> temp_v(n+1, 0);
    for(int i=1; i<=n; i++)
    {
        int x = find(i);
        temp_w[x]++;
        temp_v[x] += c[i];
    }

    vector<int> w(1, 0), v(1, 0);
    int count = 0;
    for(int i=1; i<=n; i++)
    {
        if(parent[i] != i)
            continue;
        w.push_back(temp_w[i]);
        v.push_back(temp_v[i]);
        count++;
    }

    vector<vector<int>> dp(count+1, vector<int>(k, 0));
    for(int i=1; i<=count; i++)
    {
        for(int j=0; j<k; j++)
        {
            if(w[i] > j)
                dp[i][j] = dp[i-1][j];
            else
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i]);
        }
    }
    cout << dp[count][k-1] << '\n';
    return 0;
}

int find(int x)
{
    if(parent[x] != x)
        parent[x] = find(parent[x]);
    return parent[x];
}

void _union(int a, int b)
{
    int root_a = find(a);
    int root_b = find(b);
    parent[root_b] = root_a;
}