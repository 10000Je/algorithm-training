// no.2263: 트리의 순회 (G1)

#include <iostream>
#include <vector>
using namespace std;

int inorder[100'000] = {0};
int postorder[100'000] = {0};
int idx[100'001] = {0};

// i -> root's postorder idx
// lidx, ridx -> left, right's inorder idx
void dfs(int i, int lidx, int ridx, vector<int> &preorder);

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> inorder[i];

    for (int i = 0; i < n; i++)
        cin >> postorder[i];

    for (int i = 0; i < n; i++)
        idx[inorder[i]] = i;

    vector<int> preorder;
    dfs(n - 1, 0, n - 1, preorder);

    for (int num : preorder)
        cout << num << ' ';
    cout << '\n';
    return 0;
}

void dfs(int i, int lidx, int ridx, vector<int> &preorder)
{
    int root = postorder[i];
    preorder.push_back(root);
    if (lidx == ridx)
        return;

    int lcount = idx[root] - lidx;
    int rcount = ridx - idx[root];

    if (lcount > 0)
    {
        int left = (i - 1) - rcount;
        dfs(left, lidx, idx[root] - 1, preorder);
    }

    if (rcount > 0)
    {
        int right = i - 1;
        dfs(right, idx[root] + 1, ridx, preorder);
    }
}