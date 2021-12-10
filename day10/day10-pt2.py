from dataclasses import dataclass

@dataclass
class ParanChunk:
    open: str = "("
    close: str = ")"

@dataclass
class SqChunk:
    open: str = "["
    close: str = "]"


@dataclass
class AngleChunk:
    open: str = "<"
    close: str = ">"


@dataclass
class CurlyChunk:
    open: str = "{"
    close: str = "}"

def is_corrupted(line: str) -> tuple[bool, str]:
    chunk_stack: list[ParanChunk | SqChunk | AngleChunk | CurlyChunk] = []
    for char in line.strip():
        match char:
            case "(":
                chunk_stack.append(ParanChunk())
            case "[":
                chunk_stack.append(SqChunk())
            case "<":
                chunk_stack.append(AngleChunk())
            case "{":
                chunk_stack.append(CurlyChunk())
            case _:
                last_chunk = chunk_stack.pop()
                if last_chunk.close != char:
                    return True, char

    return False, "".join([c.close for c in chunk_stack])

def main(inf: str):
    # corrupt_points: dict[str, int] = {
    #     ")": 3,
    #     "]": 57,
    #     "}": 1197,
    #     ">": 25137,
    # }
    closing_points: dict[str, int] = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    closing_scores = []
    with open(inf) as input_file:
        for line in input_file:
            total_score = 0
            corrupted, char = is_corrupted(line)
            # if corrupted:   works for pt1
            #     total_score += corrupt_points[char]
            # pt2
            if not corrupted:
                for i in reversed(char):
                    total_score *= 5
                    total_score += closing_points[i]
                closing_scores.append(total_score)

    closing_scores.sort()
    return closing_scores[len(closing_scores) // 2]


if __name__ == "__main__":
    sample_result = main("day10-sample.txt")
    print(sample_result)
    assert sample_result == 288957
    full_result = main("day10-full.txt")
    print(full_result)
    assert full_result == 3042730309
