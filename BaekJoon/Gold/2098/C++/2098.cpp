// no.2098: 외판원 순회 (G1)

#include <iostream>
#define INF 100'000'000
#define MIN(a, b) ((a < b) ? a : b)
using namespace std;

int dp[16][65536] = {0};
int graph[16][16];
int n;

int dfs(int init, int cur, int visit);

int main() 
{
    cin >> n;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
            cin >> graph[i][j];
    }
    
    for(int i=0; i<16; i++)
    {
        for(int j=0; j<65536; j++)
            dp[i][j] = -1;
    }
    
    cout << dfs(0, 0, 1<<0) << '\n';
    return 0;
}

int dfs(int init, int cur, int visit)
{
    if(visit == (1<<n)-1)
    {
        if(graph[cur][init] == 0)
            return INF;
        else
            return graph[cur][init];
    }  
    int ret = INF;
    for(int i=0; i<n; i++)
    {
        if(graph[cur][i] == 0)
            continue; // check edge
        if(visit&(1<<i))
            continue; // check already visit
        if(dp[i][visit|(1<<i)] == -1)
            dp[i][visit|(1<<i)] = dfs(init, i, visit|(1<<i));
        ret = MIN(ret, graph[cur][i] + dp[i][visit|(1<<i)]);       
    }
    return ret;
}