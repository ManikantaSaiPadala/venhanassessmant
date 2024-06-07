from typing import List

def read_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

if __name__ == "__main__":
    file_path = "sample.txt"  

    try:
        lines = read_file(file_path)
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")