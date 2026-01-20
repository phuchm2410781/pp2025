import curses

def input_box(self,prompt):
    curses.echo()
    self.stdscr.addstr(prompt)
    self.stdscr.clrtoeol()
    value = self.stdscr.getstr().decode()
    curses.noecho()
    self.stdscr.addstr("\n")
    return value