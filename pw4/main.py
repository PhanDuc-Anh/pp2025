import curses
from syst import Sys
from menu import draw_menu


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    terminal = Sys(stdscr)
    current_row = 0

    while True:
        draw_menu(stdscr, current_row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 6:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                terminal.input_student()
            elif current_row == 1:
                terminal.input_course()
            elif current_row == 2:
                terminal.input_marks()
            elif current_row == 3:
                terminal.list_student()
            elif current_row == 4:
                terminal.list_course()
            elif current_row == 5:
                terminal.list_marks()
            elif current_row == 6:
                stdscr.clear()
                h, w = stdscr.getmaxyx()
                msg = "Mayonnaise on the escalator, it's going upstairs, so see ya later!"
                stdscr.addstr(h // 2, w // 2 - len(msg) // 2, msg, curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()
                break


if __name__ == "__main__":
    curses.wrapper(main)
