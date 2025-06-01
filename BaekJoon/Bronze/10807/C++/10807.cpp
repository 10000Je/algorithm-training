// no.10807: 개수 세기 (B5)

#include <cstdio>
#include <sstream>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    getchar();
    char str[int(1e4)];
    fgets(str, int(1e4), stdin);
    istringstream iss(str);

    int nums[100];
    string buffer;
    int i=0;
    while(getline(iss, buffer, ' ')) {
        nums[i++] = stoi(buffer);
    }

    int v;
    scanf("%d", &v);

    int cnt=0;
    for(int i=0; i<n; i++) {
        if(nums[i]==v)
            cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}