#include <stdio.h>

int v[51][51];
int arr[51][51];
int n, L, R;
int max;
int count;
int dy[4] = {1, 0, 0, -1};
int dx[4] = {0, 1, -1, 0};
int idx = 1;
int flag;
int st[10000000];


int abs(int k)
{
    return (k < 0 ? -k : k);
}

void init_v()
{
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            v[i][j] = 0;
        }
    }
}

int check(int y, int x, int num)
{
    if (y == n || x == n || y == -1 || x == -1)
        return 0;
    if (v[y][x])
        return 0;
    if (num >= L && num <= R)
        return 1;
    return 0;
}

int dfs(int y, int x)
{
    if (v[y][x])
        return 0;

    v[y][x] = idx;
    int sum = 0;
    for (int i = 0; i < 4; ++i) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (check(ny, nx, abs(arr[y][x] - arr[ny][nx]))) {
            flag = 1;
            sum += dfs(ny, nx);
        }
    }
    count++;
    return (sum + arr[y][x]);
}

int main() {
    int cnt = 0;
    scanf("%d %d %d", &n, &L, &R);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%d", &arr[i][j]);
        }
    }
    int l = 3;
    while (1) {
        flag = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                count = 1;
                max = dfs(i, j);
                if (count > 1)
                    count--;
                st[idx] = max / count;
                idx++;
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (v[i][j] && st[v[i][j]])
                    arr[i][j] = st[v[i][j]];
            }
        }
        if (flag == 0) {
            printf("%d\n", cnt);
            return 0;
        }
        cnt++;
        init_v();
    }
    return 0;
}
