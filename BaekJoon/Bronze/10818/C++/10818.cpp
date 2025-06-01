// no.10818: 최소, 최대 (B3)

#include <cstdio>
#include <sstream>
#include <string>
using namespace std;

// c++ 에서는 지역(Local)내에서의 배열 최대크기가 제한되어있다. 25만 정도로..
// 따라서 매우 큰 사이즈의 배열이 필요할 때는 전역변수로 설정해주자.
// 추가로 백준에서는 이런거 상관없이 지역변수로 크게해서 제출해도 통과된다.
char str[int(1e7)];

int main() {
    int n;
    scanf("%d", &n);
    getchar();
    fgets(str, int(1e7), stdin);
    stringstream ss(str);
    
    int min = int(1e7);
    int max = -int(1e7);
    string buffer;
    while(ss >> buffer) {
        int num = stoi(buffer);
        if(num > max) {
            max = num;
        }
        if(num < min) {
            min = num;
        }
    }
    
    printf("%d %d\n", min, max);
    return 0;
}