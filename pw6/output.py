def draw(stdscr,lines):
    stdscr.clear()
    for i, line in enumerate(lines):
        stdscr.addstr(i,0,line)
    stdscr.refresh()