// no.2798: 블랙잭 (B2)

#include <cstdio>
#include <sstream>
#include <string>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    getchar();

    char str[1000];
    fgets(str, 1000, stdin);
    stringstream ss(str);

    string temp;
    int nums[100];
    int idx = 0;
    while(ss >> temp) {
        nums[idx++] = stoi(temp);
    }
    int sum = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            for(int k=0; k<n; k++) {
                if(i==j || j==k || k==i)
                    continue;
                if(nums[i]+nums[j]+nums[k] > m)
                    continue;
                if(m-(nums[i]+nums[j]+nums[k]) < m-sum)
                    sum = nums[i]+nums[j]+nums[k];
            }
        }
    }
    printf("%d\n", sum);
    return 0;
}