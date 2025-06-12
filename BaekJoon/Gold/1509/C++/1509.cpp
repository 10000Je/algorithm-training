// no.1509: 팰린드롬 분할

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define INF 2500
using namespace std;

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    string str;
    cin >> str;

    int n = str.length();
    vector<vector<bool>> check(n, vector<bool>(n, false));
    for(int i=0; i<n; i++)
        check[i][i] = true;

    for(int i=0; i<n-1; i++)
        check[i][i+1] = (str[i] == str[i+1]);

    for(int i=2; i<n; i++)
    {
        for(int j=0; j<n-i; j++)
            check[j][j+i] = (check[j+1][j+i-1] && str[j] == str[j+i]);
    }
    
    vector<int> dp(n, 0);
    for(int i=0; i<n; i++)
    {
        dp[i] = check[0][i] ? 1 : INF;
        for(int j=1; j<=i; j++)
        {
            if(check[j][i])
                dp[i] = min(dp[i], dp[j-1]+1);
        } 
    }
    cout << dp[n-1] << '\n';
    return 0;
}