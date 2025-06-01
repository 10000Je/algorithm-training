// no.1181: 단어 정렬 (S5)

#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    unordered_set<string> key;
    vector<string> arr;
    for(int i=0; i<n; i++) {
        char str[100];
        scanf("%s", str);
        if(key.find(str) == key.end()) {
            key.insert(str);
            arr.push_back(str);
        }
    }
    sort(arr.begin(), arr.end(), [](string a, string b) {
        if(a.length() < b.length()) {
            return true;
        } else if(a.length() > b.length()) {
            return false;
        } else {
            if(a.compare(b) < 0) {
                return true;
            } else {
                return false;
            }
        }
    });

    for(string str : arr) {
        printf("%s\n", str.c_str());
    }
    return 0;
}