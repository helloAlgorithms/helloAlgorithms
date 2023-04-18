import java.util.*;
class _150366 {
    static ArrayList<String> result;
    static Cell[][] map;
    static class Cord {
        int x;
        int y;
        Cord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(this.x) + Objects.hash(this.y);
        }

        @Override
        public boolean equals(Object o) {
            Cord c = (Cord)o;
            return (c.x == this.x && c.y == this.y);
        }
    }

    static class Cell {
        Cord cord;
        String value;
        Set<Cord> merged;

        Cell (Cord cord) {
            this.cord = cord;
            value = "";
            merged = new HashSet<>();
        }

        void update(String value) {
            this.value = value;
            if (merged.size() > 0) {
                for (Cord elem : merged) map[elem.x][elem.y].value = value;
            }
        }


        void merge(Cord cord) {
            if (cord.x == this.cord.x && cord.y == this.cord.y) return ;
            merged.add(this.cord);
            merged.add(cord);
            this.merged.addAll(map[cord.x][cord.y].merged);
            String target;
            if (this.value.length() == 0) target = map[cord.x][cord.y].value;
            else if (map[cord.x][cord.y].value.length() == 0) target = this.value;
            else target = this.value;
            for (Cord elem : merged) {
                if (elem.x != this.cord.x || elem.y != this.cord.y) map[elem.x][elem.y].merged = new HashSet<>(this.merged);
            }
            this.update(target);
        }

        void unmerge() {
            for (Cord elem : merged) {
                if (elem.x != this.cord.x || elem.y != this.cord.y) {
                    map[elem.x][elem.y] = new Cell(new Cord(elem.x, elem.y));
                }
            }
            merged.clear();
        }

        void print() {
            if (this.value.length() == 0) result.add("EMPTY");
            else result.add(this.value);
        }
    }

    public static void main(String[] args) {
        String[] commands = new String[]{"UPDATE 1 1 FIRST", "MERGE 1 1 1 2", "MERGE 1 2 1 3", "MERGE 2 1 1 1", "PRINT 2 1", "PRINT 1 2", "PRINT 13 1"};
        result = new ArrayList<>();
        map = new Cell[51][51];
        for (int i = 0; i < 51; i++) {
            for (int j = 0; j < 51; j++) map[i][j] = new Cell(new Cord(i, j));
        }
        for (String line : commands) {
            String[] tmp = line.split(" ");
            String cmd = tmp[0];
            int size = tmp.length;
            if (cmd.equals("UPDATE")) {
                if (size == 4) {
                    int r = Integer.parseInt(tmp[1]);
                    int c = Integer.parseInt(tmp[2]);
                    map[r][c].update(tmp[3]);
                } else {
                    for (int i = 0; i < map.length; i++) {
                        for (int j = 0; j < map[0].length; j++) {
                            if (map[i][j].value.equals(tmp[1])) map[i][j].update(tmp[2]);
                        }
                    }
                }
            } else if (cmd.equals("MERGE")) {
                int r1 = Integer.parseInt(tmp[1]);
                int c1 = Integer.parseInt(tmp[2]);
                int r2 = Integer.parseInt(tmp[3]);
                int c2 = Integer.parseInt(tmp[4]);
                map[r1][c1].merge(new Cord(r2, c2));
            } else if (cmd.equals("UNMERGE")) {
                int r = Integer.parseInt(tmp[1]);
                int c = Integer.parseInt(tmp[2]);
                map[r][c].unmerge();
            } else if (cmd.equals("PRINT")) {
                int r = Integer.parseInt(tmp[1]);
                int c = Integer.parseInt(tmp[2]);
                map[r][c].print();
            }
            for (int i = 1; i <= 3; i++) {
                for (int j = 1; j <= 3; j++) {
                    if (map[i][j].value.length() != 0) System.out.print(map[i][j].value + " ");
                    else System.out.print("EMPTY ");
                }
                System.out.println();
            }
            System.out.println();
        }
        String[] answer = new String[result.size()];
        for (int i = 0; i < result.size(); i++) answer[i] = result.get(i);
        System.out.println("fin");
    }
}