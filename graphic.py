import curses

def inicia_curses():
    stdscr=curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    return stdscr

def finaliza_curses(stdscr):
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
    return 0


