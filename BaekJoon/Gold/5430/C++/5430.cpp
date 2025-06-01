// no.5430: AC (G5)

#include <cstdio>
#include <cstring>
#include <deque>
#include <string>
#include <sstream>
#include <cstdlib>
using namespace std;

char p[500'000];
char x[500'000];

int main() {
    int t;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        deque<int> nums;
        scanf("%s", p);
        int n;
        scanf("%d", &n);
        scanf("%s", x);
        string str = x;
        str = str.substr(1, str.length()-2);
        if(!str.empty()) {
            stringstream ss(str);
            string buffer;
            while(getline(ss, buffer, ',')) {
                nums.push_back(stoi(buffer));
            }
        }
        bool reverse = false;
        bool error = false;
        for(int j=0; p[j]!=0; j++) {
            if(p[j]=='R') {
                reverse = !reverse;
            }
            else {
                if(nums.empty()) {
                    error = true;
                    break;
                }
                if(reverse) {
                    nums.pop_back();
                }
                else {
                    nums.pop_front();
                }
            }
        }
        if(error) {
            printf("error\n");
        }
        else {
            printf("[");
            if(reverse) {
                for(deque<int>::reverse_iterator iter=nums.rbegin(); iter!=nums.rend(); iter++) {
                    if(iter+1 == nums.rend()) {
                        printf("%d", *iter);
                    }
                    else {
                        printf("%d,", *iter);
                    }
                }
            }
            else {
                for(deque<int>::iterator iter=nums.begin(); iter!=nums.end(); iter++) {
                    if(iter+1 == nums.end()) {
                        printf("%d", *iter);
                    }
                    else {
                        printf("%d,", *iter);
                    }
                }
            }
            printf("]\n");
        }
    }
    return 0;
}