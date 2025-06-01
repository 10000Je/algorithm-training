// no.18110: solved.ac (S4)

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> comments;
    for(int i=0; i<n; i++) {
        int diff;
        scanf("%d", &diff);
        comments.push_back(diff);
    }
    if(n==0) {
        printf("0\n");
        return 0;
    }
    sort(comments.begin(), comments.end());
    int cut = (int)floor(comments.size() * 0.15 + 0.5);
    int sum = 0;
    for(int i=cut; i<n-cut; i++) {
        sum += comments[i];
    }
    printf("%d\n", (int)floor((double)sum/(n-cut*2)+0.5));
    return 0; 
}