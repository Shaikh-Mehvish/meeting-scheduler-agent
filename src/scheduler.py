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


def find_common_slots(compressed_calendar):
    """
    Find common overlapping time slots for all participants per day.
    """
    common_slots = {}

    for day, slots in compressed_calendar.items():
        if len(slots) < 2:
            continue

        start_time = max(slot["start"] for slot in slots)
        end_time = min(slot["end"] for slot in slots)

        if start_time < end_time:
            common_slots[day] = {
                "start": start_time,
                "end": end_time,
                "participants": [slot["person"] for slot in slots],
                "preferences": [slot["preference"] for slot in slots]
            }

    return common_slots


if __name__ == "__main__":
    data = load_availability("data/availability.json")
    compressed_calendar = compress_calendar(data)
    common_slots = find_common_slots(compressed_calendar)

    print("\nSuggested Common Meeting Slots:")
    for day, slot in common_slots.items():
        print(
            f"{day}: {slot['start']} - {slot['end']} "
            f"with participants {slot['participants']}"
        )
