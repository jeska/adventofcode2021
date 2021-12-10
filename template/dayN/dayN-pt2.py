def main(inf: str):
    with open(inf) as input_file:
        pass

    return 0


if __name__ == "__main__":
    sample_result = main("dayN-sample.txt")
    print(sample_result)
    assert sample_result == 0
    # full_result = main("dayN-full.txt")
    # print(full_result)
    # assert full_result == 0
