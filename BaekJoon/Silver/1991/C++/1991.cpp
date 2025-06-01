// no.1991: 트리 순회 (S1)

#include <cstdio>
#include <vector>
using namespace std;

void preorder(vector<vector<int>>&, int);
void inorder(vector<vector<int>>&, int);
void postorder(vector<vector<int>>&, int);

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> tree(n, vector<int>(2, -1));
    for(int i=0; i<n; i++) {
        getchar();
        char node, left, right;
        scanf("%c %c %c", &node, &left, &right);
        if(left != '.')
            tree[node-'A'][0] = left-'A';
        if(right != '.')
            tree[node-'A'][1] = right-'A';
    }
    preorder(tree, 0);
    printf("\n");
    inorder(tree, 0);
    printf("\n");
    postorder(tree, 0);
    printf("\n");
    return 0;
}

void preorder(vector<vector<int>>& tree, int root) {
    printf("%c", root+'A');
    if(tree[root][0] != -1)
        preorder(tree, tree[root][0]);
    if(tree[root][1] != -1)
        preorder(tree, tree[root][1]);
}

void inorder(vector<vector<int>>& tree, int root) {
    if(tree[root][0] != -1)
        inorder(tree, tree[root][0]);
    printf("%c", root+'A');
    if(tree[root][1] != -1)
        inorder(tree, tree[root][1]);
}

void postorder(vector<vector<int>>& tree, int root) {
    if(tree[root][0] != -1)
        postorder(tree, tree[root][0]);
    if(tree[root][1] != -1)
        postorder(tree, tree[root][1]);
    printf("%c", root+'A');
}