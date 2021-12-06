from dataclasses import dataclass


@dataclass
class LanternFish:
    internal_timer: int = 8

    def decrement_timer(self):
        self.internal_timer -= 1

    def __repr__(self):
        return f"{self.internal_timer}"


def main(inf: str):
    with open(inf) as input_file:
        lantern_fishies = [
            LanternFish(internal_timer=int(i)) for i in input_file.readline().split(",")
        ]

    for i in range(0, 80):
        new_fishes = []
        for lf in lantern_fishies:
            lf.decrement_timer()
            if lf.internal_timer == -1:
                lf.internal_timer = 6
                new_fishes.append(LanternFish())

        lantern_fishies = lantern_fishies + new_fishes

    return len(lantern_fishies)


if __name__ == "__main__":
    sample_result = main("day6-sample.txt")
    print(sample_result)
    assert sample_result == 5934
    full_result = main("day6-full.txt")
    print(full_result)
    assert full_result == 374994
