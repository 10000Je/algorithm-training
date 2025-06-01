// no.1259: 팰린드롬수 (B1)

#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    while(true) {
        char str[10];
        fgets(str, 10, stdin);
        int l = strlen(str);
        str[--l] = '\0';
        if(strcmp(str, "0") == 0)
            return 0;
        int lptr=0, rptr=l-1;
        bool isPalindrome = true;
        while(lptr <= rptr) {
            if(str[lptr] != str[rptr]) {
                isPalindrome = false;
                break;
            }
            lptr++;
            rptr--;
        }
        if(isPalindrome) {
            printf("yes\n");
        } else {
            printf("no\n");
        }
    }
    return 0;
}