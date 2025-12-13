import curses


def draw_menu(stdscr, current_row):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    menu = [
        "Input Student Info",
        "Input Course Info",
        "Input Marks",
        "List Students",
        "List Courses",
        "List Marks",
        "Exit"
    ]

    title = "School System Terminal"
    title_y = h // 2 - len(menu) // 2 - 4

    stdscr.addstr(title_y, w // 2 - len(title) // 2 - 2, "=" * (len(title) + 4), curses.A_BOLD)
    stdscr.addstr(title_y + 1, w // 2 - len(title) // 2 - 1, f" {title} ", curses.A_BOLD)
    stdscr.addstr(title_y + 2, w // 2 - len(title) // 2 - 2, "=" * (len(title) + 4), curses.A_BOLD)

    for idx, item in enumerate(menu):
        x = w // 2 - len(item) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == current_row:
            stdscr.addstr(y, x - 2, f"> {item} <", curses.A_REVERSE | curses.A_BOLD)
        else:
            stdscr.addstr(y, x, item)

    hint = "Use UP/DOWN arrows to navigate, ENTER to select"
    stdscr.addstr(h - 2, w // 2 - len(hint) // 2, hint, curses.A_DIM)
    stdscr.refresh()
