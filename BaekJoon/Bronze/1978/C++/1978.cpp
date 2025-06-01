// no.1978: 소수 찾기 (B2)

#include <cstdio>
#include <sstream>
using namespace std;

bool isPrime(int num);

int main() {
    int n;
    scanf("%d", &n);
    char str[10000];
    getchar();
    fgets(str, 10000, stdin);
    stringstream ss(str);
    string tmp;
    int count = 0;
    while(ss >> tmp) {
        if(isPrime(stoi(tmp)))
            count++;
    }
    printf("%d\n", count);
    return 0;
}

bool isPrime(int num) {
    if(num == 1)
        return false;
    for(int i=2; i<num; i++) {
        if(num%i == 0) {
            return false;
        }
    }
    return true;
}