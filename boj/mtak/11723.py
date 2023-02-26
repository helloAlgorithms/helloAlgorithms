opcnt = int(input())
s = 0
def _add(x):
    global s
    s|=(1<<x)
def _remove(x):
    global s
    s&=~(1<<x)
def _check(x):
    print(int(s & x))
def _toggle(x):
    global s
    s^=(1<<x)
def _all():
    global s
    s = (1<<21) - 1
def _empty():
    global s
    s = 0
tool = {"add":_add, "remove":_remove, "check":_check, "toggle":_toggle, "all":_all, "empty":_empty}

for _ in range(opcnt):
    cmd = input().split()
    if len(cmd) == 2:
        tool[cmd[0]](int(cmd[1]))
    else:
        tool[cmd[0]]()
