from typing import List

def write_file(file_path: str, lines: List[str]) -> None:
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


if __name__ == "__main__":
    file_path = "output.txt"  
    lines_to_write = [
        "First line",
        "Second line",
        "Third line"
    ]

    write_file(file_path, lines_to_write)
    print(f"Lines written to {file_path}.")