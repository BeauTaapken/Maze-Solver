from line import Line
from point import Point


class Cell():
    def __init__(self, win=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if not self.win:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._draw_wall(Point(self._x1, self._y1), Point(self._x1, self._y2), self.has_left_wall)

        self._draw_wall(Point(self._x2, self._y1), Point(self._x2, self._y2), self.has_right_wall)

        self._draw_wall(Point(self._x1, self._y1), Point(self._x2, self._y1), self.has_top_wall)

        self._draw_wall(Point(self._x1, self._y2), Point(self._x2, self._y2), self.has_bottom_wall)

    def _draw_wall(self, start, end, draw_visible_wall):
        color = "black" if draw_visible_wall else "white"
        line = Line(start, end)
        self.win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        if not self.win:
            return
        color = "gray" if undo else "red"

        half_length = abs(self._x2 - self._x1) // 2

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2

        center_cur_cell = (half_length + self._x1, half_length + self._y1)
        center_to_cell = (half_length2 + to_cell._x1, half_length2 + to_cell._y1)

        line = Line(Point(center_cur_cell[0], center_cur_cell[1]), Point(center_to_cell[0], center_to_cell[1]))
        self.win.draw_line(line, color)

