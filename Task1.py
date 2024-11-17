import json

def task() -> float:
    input_filename = "input.json"
    with open(input_filename) as fl:
        data = json.load(fl)
        res = sum(item["score"] * item["weight"] for item in data)
    return round(res,3)

if __name__ == "__main__":
    print(task())
