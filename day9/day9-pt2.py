# refactor me, dude!

from dataclasses import dataclass
from functools import reduce


@dataclass
class HeightMapCell:
    val: int
    x: int
    y: int
    top: int
    bottom: int
    left: int
    right: int
    traversed: bool = False

    def is_local_min(self):
        return all([self.val < h for h in [self.top, self.bottom, self.left, self.right]])


def create_height_map(in_height_map: list[list[int]]):
    out_height_map: list[list[HeightMapCell]] = []
    for x, row in enumerate(in_height_map):
        out_row = []
        for y, col in enumerate(row):
            top = in_height_map[x - 1][y] if x > 0 else 99
            bottom = in_height_map[x + 1][y] if x < len(in_height_map) - 1 else 99
            left = in_height_map[x][y - 1] if y > 0 else 99
            right = in_height_map[x][y + 1] if y < len(row) - 1 else 99
            out_row.append(HeightMapCell(col, x, y, top, bottom, left, right))
        out_height_map.append(out_row)
    return out_height_map


def get_local_mins(height_map: list[list[HeightMapCell]]):
    local_mins: list[HeightMapCell] = []
    for row in height_map:
        for cell in row:
            if cell.is_local_min():
                local_mins.append(cell)
    return local_mins


def get_basin(height_map: list[list[HeightMapCell]], cell: HeightMapCell):
    cell.traversed = True
    if cell.val == 9:
        return 0
    else:
        return (
            1
            + (
                get_basin(height_map, height_map[cell.x - 1][cell.y])
                if (
                    cell.top != 99
                    # and cell.val < height_map[cell.x - 1][cell.y].val
                    and not height_map[cell.x - 1][cell.y].traversed
                )
                else 0
            )
            + (
                get_basin(height_map, height_map[cell.x + 1][cell.y])
                if (
                    cell.bottom != 99
                    # and cell.val < height_map[cell.x + 1][cell.y].val
                    and not height_map[cell.x + 1][cell.y].traversed
                )
                else 0
            )
            + (
                get_basin(height_map, height_map[cell.x][cell.y - 1])
                if (
                    cell.left != 99
                    # and cell.val < height_map[cell.x][cell.y - 1].val
                    and not height_map[cell.x][cell.y - 1].traversed
                )
                else 0
            )
            + (
                get_basin(height_map, height_map[cell.x][cell.y + 1])
                if (
                    cell.right != 99
                    # and cell.val < height_map[cell.x][cell.y - 1].val
                    and not height_map[cell.x][cell.y + 1].traversed
                )
                else 0
            )
        )


def main(inf: str):
    int_height_map: list[list[int]] = []
    with open(inf) as input_file:
        for line in input_file:
            int_height_map.append([int(i) for i in line.strip()])

    height_map = create_height_map(int_height_map)

    local_mins = get_local_mins(height_map=height_map)

    basin_sizes = []
    for local_min in local_mins:
        basin_size = get_basin(height_map, local_min)
        basin_sizes.append(basin_size)
    bs_sorted = sorted(basin_sizes)

    return reduce((lambda x, y: x * y), bs_sorted[-3:])


if __name__ == "__main__":
    sample_result = main("day9-sample.txt")
    print(sample_result)
    assert sample_result == 1134
    full_result = main("day9-full.txt")
    print(full_result)
    assert full_result == 1327014
