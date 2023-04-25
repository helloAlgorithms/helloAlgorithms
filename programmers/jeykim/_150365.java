public class _150365 {
    public String ver_1(int n, int m, int x, int y, int r, int c, int k) {
        StringBuilder answer = new StringBuilder();
        int dist = Math.abs(x - r) + Math.abs(y - c);
        if (k >= dist && (k - dist) % 2 == 0) {
            while (x < n && dist < k && k >= dist + answer.length() + 1) {
                answer.append("d");
                x++;
                dist = Math.abs(x - r) + Math.abs(y - c);
            }
            while (y > 1 && dist < k && k >= dist + answer.length() + 1) {
                answer.append("l");
                y--;
                dist = Math.abs(x - r) + Math.abs(y - c);
            }
            if (y + 1 <= m) {
                while (k >= dist + answer.length() + 2) {
                    answer.append("rl");
                }
            }
            int x_dist = x - r;
            int y_dist = y - c;
            if (x_dist >= 0) {
                // 좌우 먼저 맞추기
                if (y_dist < 0) for (int i = 0; i < Math.abs(y_dist); i++) answer.append("r");
                else for (int i = 0; i < Math.abs(y_dist); i++) answer.append("l");
                for (int i = 0; i < Math.abs(x_dist); i++) answer.append("u");
            } else {
                // 아래로 먼저 맞추기
                for (int i = 0; i < Math.abs(x_dist); i++) answer.append("d");
                if (y_dist < 0) for (int i = 0; i < Math.abs(y_dist); i++) answer.append("r");
                else for (int i = 0; i < Math.abs(y_dist); i++) answer.append("l");
            }
            if (answer.length() < k) {
                if (r + 1 <= n) while (answer.length() + 2 <= k) answer.append("du");
                if (c - 1 >= 1) while (answer.length() + 2 <= k) answer.append("lr");
                if (c + 1 <= m) while (answer.length() + 2 <= k) answer.append("rl");
                if (r - 1 >= 1) while (answer.length() + 2 <= k) answer.append("ud");
            }
            return answer.toString();
        }
        else return "impossible";
    }
    public String ver2(int n, int m, int x, int y, int r, int c, int k) {
        StringBuilder sb = new StringBuilder();
        int dist = Math.abs(x - r) + Math.abs(y - c);
        if (k >= dist && (k - dist) % 2 == 0) {
            while (k-- > 0) {
                int downX = x + 1, leftY = y - 1, rightY = y + 1, upX = x - 1;
                if (downX <= n && Math.abs(downX - r) + Math.abs(y - c) <= k) {
                    x = downX;
                    sb.append('d');
                } else if (leftY >= 1 && Math.abs(x - r) + Math.abs(leftY - c) <= k) {
                    y = leftY;
                    sb.append('l');
                } else if (rightY <= m && Math.abs(x - r) + Math.abs(rightY - c) <= k) {
                    y = rightY;
                    sb.append('r');
                } else if (upX >= 1 && Math.abs(upX - r) + Math.abs(y - c) <= k) {
                    x = upX;
                    sb.append('u');
                }
            }
            return sb.toString();
        }
        else return "impossible";
    }
}
