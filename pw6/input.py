import curses
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def input_box(stdscr,prompt):
    curses.echo()
    stdscr.addstr(prompt)
    stdscr.clrtoeol()
    value = stdscr.getstr().decode()
    curses.noecho()
    stdscr.addstr("\n")
    return value