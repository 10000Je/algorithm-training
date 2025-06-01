// no.1436: 영화감독 숌 (S5)

#include <cstdio>
#include <string>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    int i=0;
    int num=0;
    while(i<n) {
        num++;
        if(to_string(num).find("666") != string::npos) {
            i++;
        }
    }
    printf("%d\n", num);
    return 0;
}