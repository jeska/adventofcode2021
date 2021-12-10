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


def main(inf: str):
    points: dict[str, int] = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    total_score = 0
    with open(inf) as input_file:
        for line in input_file:
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
                            total_score += points[char]
                            break

    return total_score


if __name__ == "__main__":
    sample_result = main("day10-sample.txt")
    print(sample_result)
    assert sample_result == 26397
    full_result = main("day10-full.txt")
    print(full_result)
    assert full_result == 311949
