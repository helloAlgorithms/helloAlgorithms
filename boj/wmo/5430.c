#include <stdio.h>

int deque[2000001];
int head = 1000000;
int tail = 1000000;

void push_front(int n) {
    deque[--head] = n;
}

void push_back(int n) {
    deque[tail++] = n;
}

void pop_front() {
    head++;
}

void pop_back() {
    tail--;
}

int atoi(char *str) {
    int result = 0;
    while (*str && *str != ',' && *str != ']') {
        if (*str == '[') {
            str++;
            continue;
        }
        result = (result *  10) + (*str - 48);
        str++;
    }
    return result;
}

int main() {
    int t, n, i;
    int flag = 0;
    char str[1000002];
    char temp[1000002];
    scanf("%d", &t);
    while (t--) {
        head = 1000000;
        tail = 1000000;
        flag = 0;
        scanf("%s", str);
        scanf("%d", &n);
        scanf("%s", temp);
        i = 0;
        while (n--) {
            while (1) {
                if (temp[i] > 47 && temp[i] < 58)
                    break;
                i++;
            }
            push_back(atoi(&temp[i]));
            while (1) {
                if (temp[i] < 48 || temp[i] > 57)
                    break;
                i++;
            }
        }
        i = 0;
        while (str[i]) {
            if (str[i] == 'R') {
                if (!flag)
                    flag = 1;
                else
                    flag = 0;
            }
            else if (str[i] == 'D' && !flag)
                pop_front();
            else if (str[i] == 'D' && flag)
                pop_back();
            i++;
        }
        if (tail - head < 0)
            printf("error\n");
        else if (tail - head == 0)
            printf("[]\n");
        else {
            printf("[");
            if (!flag) {
                for (int j = head; j < tail - 1; ++j) {
                    printf("%d,", deque[j]);
                }
                printf("%d]\n", deque[tail - 1]);
            }
            else {
                for (int j = tail - 1; j > head; --j) {
                    printf("%d,", deque[j]);
                }
                printf("%d]\n", deque[head]);
            }
        }
    }
    return 0;
}
