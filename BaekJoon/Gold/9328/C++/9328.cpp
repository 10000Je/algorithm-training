// no.9238: 열쇠 (G1)

#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <utility>

using namespace std;

int bfs(const vector<vector<char>> &graph, int check);

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int h, w;
        cin >> h >> w;

        vector graph(h + 2, vector(w + 2, '.'));
        for (int j = 1; j <= h; j++)
        {
            string str;
            cin >> str;
            for (size_t k = 1; k <= str.length(); k++)
                graph[j][k] = str[k - 1];
        }
        string str{};
        cin >> str;
        int check = 0;
        for (char key : str)
        {
            int idx = key - 'a';
            check = (check | (1 << idx));
        }
        int count = bfs(graph, check);
        cout << count << '\n';
    }
    return 0;
}

int bfs(const vector<vector<char>> &graph, int check)
{
    size_t n = graph.size();
    size_t m = graph[0].size();

    queue<pair<int, int>> que{};
    vector visit(n, vector<bool>(m, false));

    int size = 'Z' - 'A' + 1;
    vector doors(size, stack<pair<int, int>>{});

    que.push(pair{0, 0});
    visit[0][0] = true;

    int total = 0;

    while (!que.empty())
    {
        auto [r, c] = que.front();
        que.pop();
        vector nodes{
            pair{r - 1, c}, pair{r + 1, c},
            pair{r, c - 1}, pair{r, c + 1}};

        for (auto node : nodes)
        {
            auto [nr, nc] = node;
            if (nr < 0 || nr >= n || nc < 0 || nc >= m)
                continue;

            if (visit[nr][nc])
                continue;

            if (graph[nr][nc] == '*')
                continue;

            if (graph[nr][nc] == '$')
                total += 1;

            if ('a' <= graph[nr][nc] && graph[nr][nc] <= 'z')
            {
                int idx = graph[nr][nc] - 'a';
                if ((check & (1 << idx)) == 0)
                {
                    check = (check | (1 << idx));
                    auto &door = doors[idx];
                    while (!door.empty())
                    {
                        que.push(door.top());
                        door.pop();
                    }
                }
            }

            if ('A' <= graph[nr][nc] && graph[nr][nc] <= 'Z')
            {
                int diff = 'A' - 'a';
                int idx = graph[nr][nc] - diff - 'a';
                if ((check & (1 << idx)) == 0)
                {
                    doors[idx].push(pair{nr, nc});
                    continue;
                }
            }

            visit[nr][nc] = true;
            que.push(pair{nr, nc});
        }
    }
    return total;
}