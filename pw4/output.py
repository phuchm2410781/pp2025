def draw(self,lines):
    self.stdscr.clear()
    for i, line in enumerate(lines):
        self.stdscr.addstr(i,0,line)
    self.stdscr.refresh()