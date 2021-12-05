from dataclasses import dataclass
from collections import defaultdict


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


@dataclass(eq=True, frozen=True)
class Path:
    start: Point
    end: Point

    def is_straight_line(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def get_points(self):
        points = []
        if self.start.x == self.end.x:
            x = self.start.x
            y_step = 1 if self.start.y <= self.end.y else -1
            for y in range(self.start.y, self.end.y + y_step, y_step):
                points.append(Point(x=x, y=y))
            return points
        elif self.start.y == self.end.y:
            y = self.start.y
            x_step = 1 if self.start.x <= self.end.x else -1
            for x in range(self.start.x, self.end.x + x_step, x_step):
                points.append(Point(x=x, y=y))
            return points


def parse_path(path: str):
    start_str, end_str = path.split()[0], path.split()[2]
    start_point = Point(x=int(start_str.split(",")[0]), y=int(start_str.split(",")[1]))
    end_point = Point(x=int(end_str.split(",")[0]), y=int(end_str.split(",")[1]))
    return Path(start=start_point, end=end_point)


def main():
    paths: list[Path] = []
    with open("day5-full.txt") as input_file:
        for line in input_file:
            path = parse_path(line)
            if path.is_straight_line():
                paths.append(path)

    points: dict[Point, int] = defaultdict(int)
    for path in paths:
        for point in path.get_points():
            points[point] += 1

    print([k for k, v in points.items() if v > 1])
    print(len([k for k, v in points.items() if v > 1]))


if __name__ == "__main__":
    main()
