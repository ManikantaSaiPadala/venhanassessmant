import csv
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]


if __name__ == "__main__":
    file_path = "sample.csv"  

    rows = read_csv(file_path)
    for row in rows:
        print(row)