import json
from collections import defaultdict


def load_availability(file_path):
    """
    Load availability data from JSON file.
    """
    with open(file_path, "r") as f:
        return json.load(f)


def compress_calendar(data):
    """
    Compress calendar data by grouping availability by day.
    This removes redundancy and prepares data for scheduling.
    """
    compressed = defaultdict(list)

    for person in data:
        name = person["person"]
        preference = person["preference"]

        for slot in person["availability"]:
            day = slot["day"]
            compressed[day].append({
                "person": name,
                "start": slot["start"],
                "end": slot["end"],
                "preference": preference
            })

    return compressed


if __name__ == "__main__":
    data = load_availability("data/availability.json")
    compressed_calendar = compress_calendar(data)

    print("Compressed Calendar Data:")
    for day, slots in compressed_calendar.items():
        print(f"\n{day}:")
        for slot in slots:
            print(slot)

