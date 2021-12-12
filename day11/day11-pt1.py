from dataclasses import dataclass
from math import sqrt


@dataclass
class DumboOctopus:
    energy_level: int
    has_flashed: bool = False


def get_neighbors(n: int, s: int) -> list[DumboOctopus]:
    neighbors = []
    if n - s >= 0:  # get previous row
        neighbors.append(n - s)
        if n % s != 0:  # get prev col
            neighbors.append(n - s - 1)
        if n % s != (s - 1):  # get next col
            neighbors.append(n - s + 1)
    if n + s < s ** 2:  # get next row
        neighbors.append(n + s)
        if n % s != 0:  # get prev col
            neighbors.append(n + s - 1)
        if n % s != (s - 1):  # get next col
            neighbors.append(n + s + 1)
    if n % s != 0:  # get prev col
        neighbors.append(n - 1)
    if n % s != (s - 1):  # get next col
        neighbors.append(n + 1)
    return sorted(neighbors)


def get_flashers(octopi: list[DumboOctopus]):
    flashed_octopi = [(i, o) for (i, o) in enumerate(octopi) if o.energy_level >= 9 and not o.has_flashed]
    for (idx, octopus) in flashed_octopi:
        octopus.has_flashed == True
        octopi[idx] = octopus


def energy_up(o: DumboOctopus, i: int, flashers: list[int], first_pass: bool = True):
    if o.energy_level != 0 or first_pass:
        o.energy_level = (o.energy_level + 1) % 10
        if o.energy_level == 0:
            flashers.append(i)


def print_garden(octopus_garden: list[DumboOctopus], w: int):
    for i in range(0, w):
        row_str = ""
        for j in range(0, w):
            row_str += str(octopus_garden[i * w + j].energy_level)
        print(row_str)


def main(inf: str, num_steps: int = 100):
    octopus_garden: list[DumboOctopus] = []
    with open(inf) as input_file:
        for line in input_file:
            octopus_garden += [DumboOctopus(energy_level=int(o)) for o in line.strip()]
    w = int(sqrt(len(octopus_garden)))

    total_flashes = 0
    for _ in range(0, num_steps):
        flashers = []
        for i, o in enumerate(octopus_garden):
            energy_up(o, i, flashers)

        for flasher in flashers:
            bumpos = get_neighbors(flasher, w)
            for bumpo in bumpos:
                energy_up(octopus_garden[bumpo], bumpo, flashers, first_pass=False)

        total_flashes += len(flashers)
    return total_flashes


if __name__ == "__main__":
    small_sample_result = main("day11-sample-small.txt", 2)
    print(small_sample_result)
    assert small_sample_result == 9
    sample_result = main("day11-sample.txt", 10)
    print(sample_result)
    assert sample_result == 204
    sample_result = main("day11-sample.txt", 100)
    print(sample_result)
    assert sample_result == 1656
    full_result = main("day11-full.txt")
    print(full_result)
    # assert full_result == 0
