// no.28702: FizzBuzz (B1)

#include <cstdio>
#include <cstdlib>
using namespace std;

bool isNum(const char* str);

int main() {
    char a[10], b[10], c[10];
    int num;
    scanf("%s", a);
    scanf("%s", b);
    scanf("%s", c);
    if(isNum(a)) {
        num = atoi(a)+3;
    } else if(isNum(b)) {
        num = atoi(b)+2;
    } else {
        num = atoi(c)+1;
    }
    if(num%3==0 && num%5==0) {
        printf("FizzBuzz\n");
    } else if(num%3==0) {
        printf("Fizz\n");
    } else if(num%5==0) {
        printf("Buzz\n");
    } else {
        printf("%d\n", num);
    }
}

bool isNum(const char* str) {
    int i=0;
    while(str[i]) {
        if(str[i]<'0' || str[i]>'9') {
            return false;
        }
        i++;
    }
    return true;
}