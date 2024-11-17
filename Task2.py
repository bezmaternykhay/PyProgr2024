import csv, json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_fl:
        reader = csv.DictReader(csv_fl)
        data = [row for row in reader]
        res = json.dumps(data, indent=4)
        with open(OUTPUT_FILENAME, 'w') as json_fl:
            for item in data:
                json.dump(item ,json_fl)
    print(res,end="")

if __name__ == '__main__':
    task()