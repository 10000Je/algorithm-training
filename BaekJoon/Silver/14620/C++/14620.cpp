// no.14620: 꽃길 (S2)
/*
 * 전형적인 완전탐색 문제. 씨앗이 3개로 고정되어 있으므로
 * 3중 for문을 사용해도 되나, 구현 연습을 위해 dfs로 구현하였다.
 */
#include <cstdio>
#include <sstream>
#include <algorithm>
#define INF int(1e9);
using namespace std;

int price[10][10];
bool state[10][10];
int sum = INF;
int n;

void bruteforce(int depth=0);
void change(int i, int j, bool b);

int main() {
    scanf("%d", &n);
    getchar();
    for(int i=0; i<n; i++) {
        char str[100];
        fgets(str, 100, stdin);
        istringstream iss(str);
        string buffer;
        int j = 0;
        while(getline(iss, buffer, ' ')) {
            price[i][j++] = stoi(buffer);
        }
    }
    bruteforce();
    printf("%d\n", sum);
    return 0;
}

void bruteforce(int depth) {
    if(depth == 3) {
        int val = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(state[i][j])
                    val += price[i][j];
            }
        }
        sum = min(val, sum);
        return;
    }
    for(int i=1; i<n-1; i++) {
        for(int j=1; j<n-1; j++) {
            if(state[i-1][j] or state[i][j-1] or state[i+1][j] or state[i][j+1] or state[i][j])
                continue;
            change(i, j, true);
            bruteforce(depth+1);
            change(i, j, false);
        }
    }
    return;
}

void change(int i, int j, bool b) {
    state[i][j] = b;
    state[i+1][j] = b;
    state[i][j+1] = b;
    state[i-1][j] = b;
    state[i][j-1] = b;
}