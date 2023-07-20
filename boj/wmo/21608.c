#include <stdio.h>

int arr[21][21];
int arr2[500][5];
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
int v[1000][21];
int arr3[5] = {0, 1, 10, 100, 1000};
int n;
typedef struct {
    int t;
    int y;
    int x;
    int empty;
} St;
St s1;
St s2;

int min(int a, int b) {
    return a < b ? a : b;
}

void v_init() {
    s1.t = 0;
    s1.y = n;
    s1.x = n;
    s1.empty = 0;
    s2.t = 0;
    s2.y = n;
    s2.x = n;
    s2.empty = -1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            v[i][j] = 0;
        }
    }
}

void dfs(int y, int x, int index) {

    if (v[y][x] || y == -1 || x == -1 || y == n || x == n)
        return ;
    v[y][x] = 1;

    if (arr[y][x] == 0) {
        int a = 0;
        int b = 0;
        for (int i = 0; i < 4; i++) {
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            if (ny != -1 && nx != -1 && ny != n && nx != n) {
                if (arr[ny][nx] == 0)
                    a++;
                for (int j = 0; j < 4; j++) {
                    if (arr[ny][nx] == arr2[index][j + 1])
                        b++;
                }
            }
        }

        //1을 만족하는 경우 비교
        if (s2.empty == a) {
            if (s2.y > y) {
                s2.y = y;
                s2.x = x;
            } else if (s2.y == y) {
                s2.x = min(s2.x, x);
            }
        } else if (s2.empty < a) {
            s2.empty = a;
            s2.y = y;
            s2.x = x;
        }
        if (b == s1.t && s1.empty < a) {
            s1.empty = a;
            s1.y = y;
            s1.x = x;
        } else if (b == s1.t && s1.empty == a) {
            if (s1.y > y) {
                s1.y = y;
                s1.x = x;
            } else if (s1.y == y) {
                s1.x = min(s1.x, x);
            }
        }
        //그냥 1을 만족할 경우
        if (b > s1.t) {
            s1.y = y;
            s1.x = x;
            s1.t = b;
            s1.empty = a;
        }
    }
    for (int i = 0; i < 4; i++) {
        if (v[y + dy[i]][x + dx[i]]) continue;
            dfs(y + dy[i], x + dx[i], index);
    }
}

void solve(int index) {

    v_init();

    dfs(0, 0, index);
    if (s1.t == 0) {
        arr[s2.y][s2.x] = arr2[index][0];
    }
    else {
        arr[s1.y][s1.x] = arr2[index][0];
    }
    v_init();
}

int main() {
    int result = 0;
    scanf("%d", &n);
    for (int i = 0; i < n * n; i++)
        for (int j = 0; j < 5; j++)
            scanf("%d", &arr2[i][j]);
    for (int i = 0; i < n * n; i++)
        solve(i);

    int t = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            t = 0;
            for (int k = 0; k < 4; ++k) {
                int ny = i + dy[k];
                int nx = j + dx[k];
                if (ny != -1 && nx != -1 && ny != n && nx != n) {
                    for (int l = 0; l < n * n; ++l) {
                        if (arr[i][j] == arr2[l][0]) {
                            for (int m = 1; m < 5; ++m) {
                                if (arr[ny][nx] == arr2[l][m])
                                    t++;
                            }
                        }
                    }
                }
            }
            result += arr3[t];
        }
    }
    printf("%d\n", result);
}
