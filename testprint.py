#!/usr/bin/python

# Import some module/s
import curses

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
        stdscr.addstr(7, 0, "Hello World", curses.color_pair(1))
        stdscr.addstr(8, 0, "Red text", curses.color_pair(2))
        stdscr.addstr(9, 0, "GREEN ALERT!", curses.color_pair(3))
        stdscr.addstr(10, 0, "Boris is the biggest English traitor since Tostig Godwinson", curses.color_pair(7))
        stdscr.addstr(12, 0, "Hit any key to end program")
        stdscr.refresh()

    except curses.ERR:
        # End of screen reached
        pass

     #  Pause and wait for key press
    stdscr.getch()

# Gracefully exit curses and tidy up terminal
curses.wrapper(main)

# Standard program end with same indent as the program start
raise SystemExit
