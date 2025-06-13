// no.1562: 계단 수

#include <iostream>
#define R 1'000'000'000
using namespace std;

int dp[100][10][1024] = {0};

int main()
{
    int n;
    cin >> n;

    for(int j=1; j<10; j++)
        dp[0][j][1<<j] = 1;

    for(int i=1; i<n; i++) 
    {
        for(int j=0; j<10; j++) 
        {   
            for(int k=0; k<1024; k++)
            {   
                if((k & (1 << j)) == 0) // 불가능한 경우의 수에 대해선 연산을 진행하지 않는다.
                    continue;
                if(j > 0)
                {
                    dp[i][j][k] += (dp[i-1][j-1][k] + dp[i-1][j-1][k&(~(1<<j))])%R;
                    dp[i][j][k] %= R;
                }
                if(j < 9)
                {
                    dp[i][j][k] += (dp[i-1][j+1][k] + dp[i-1][j+1][k&(~(1<<j))])%R;
                    dp[i][j][k] %= R;
                }
            }     
        }
    }

    int sum = 0;
    for(int i=0; i<10; i++)
    {
        sum += dp[n-1][i][1023];
        sum %= R;
    }

    cout << sum << '\n';
    return 0;
}
