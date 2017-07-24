#!/usr/bin/python

# Import some modules, use pip install
import curses
import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

stdscr.addstr("Hello World")
stdscr.refresh()

try:
    while True:
        time.sleep(0.001)
except KeyboardInterrupt:
    pass

curses.nocbreak()
curses.echo()
curses.endwin()


# Python appears to need a line with same indent as the program start
raise SystemExit
