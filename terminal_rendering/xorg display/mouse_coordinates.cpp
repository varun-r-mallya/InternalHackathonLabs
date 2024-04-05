#include <ncurses.h>

int main() {
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);
    mousemask(ALL_MOUSE_EVENTS | REPORT_MOUSE_POSITION, NULL);
    printw("Click anywhere in the terminal window...\n");
    refresh();
    MEVENT event;
    while (1) {
        int ch = getch();
        if (ch == KEY_MOUSE) {
            if (getmouse(&event) == OK) {
                clear();
                printw("You clicked at (%d, %d)\n", event.x, event.y);
                refresh();
            }
        }
    }

    // Cleanup
    endwin();
    return 0;
}
