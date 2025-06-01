// no.1541: 잃어버린 괄호 (S2)

#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

int main() {
    char str[51];
    scanf("%s", str);
    
    string tmp;
    int i=0, cur=0, ret=0;
    bool sign = false;
    while(true) {
        if(str[i]=='\0' || str[i]=='+' || str[i]=='-') {
            cur += stoi(tmp);
            tmp.clear();
            if(str[i]=='-' || str[i]=='\0') {
                if(!sign) {
                    ret += cur;
                    sign = true;
                } else {
                    ret -= cur;
                }
                cur = 0;
                if(str[i]==0)
                    break;
            }
        } else {
            tmp += str[i];
        }
        i++;
    }
    printf("%d\n", ret);
    return 0;
}