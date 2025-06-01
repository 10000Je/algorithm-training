// no.2920: 음계 (B2)

#include <cstdio>
#include <sstream>
using namespace std;

int main() {
    char str[100];
    fgets(str, 100, stdin);
    stringstream ss(str);
    string curLetter;
    ss >> curLetter;
    if(curLetter == "1") {
        int i=2;
        while(ss >> curLetter) {
            int curNum = stoi(curLetter);
            if(curNum != i++) {
                printf("mixed\n");
                return 0;
            }
        }
        printf("ascending\n");
    } else {
        if(curLetter != "8") {
            printf("mixed\n");
            return 0;
        }
        else {
            int i=7;
            while(ss >> curLetter) {
                int curNum = stoi(curLetter);
                if(curNum != i--) {
                    printf("mixed\n");
                    return 0;
                }
            }
        }
        printf("descending\n");
    }
    return 0;
}