// no.2164: 카드2 (S4)

#include <cstdio>
#include <queue>
using namespace std;

int main() {
    queue<int> cards;
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        cards.push(i);
    }
    int lastCard;
    while(true) {
        lastCard = cards.front();
        cards.pop();
        if(cards.empty())
            break;
        int temp = cards.front();
        cards.pop();
        cards.push(temp);
    }
    printf("%d\n", lastCard);
    return 0;
}