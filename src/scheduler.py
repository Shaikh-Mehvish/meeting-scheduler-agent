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


def get_time_category(start_time):
    """
    Convert start time to time category.
    """
    if 9 <= start_time < 12:
        return "morning"
    elif 12 <= start_time < 16:
        return "afternoon"
    else:
        return "evening"


def rank_slots(common_slots):
    """
    Rank meeting slots based on participant time preferences.
    """
    ranked = []

    for day, slot in common_slots.items():
        time_category = get_time_category(slot["start"])
        score = 0

        for pref in slot["preferences"]:
            if pref == time_category:
                score += 1

        ranked.append({
            "day": day,
            "start": slot["start"],
            "end": slot["end"],
            "participants": slot["participants"],
            "score": score
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


if __name__ == "__main__":
    data = load_availability("data/availability.json")
    compressed_calendar = compress_calendar(data)
    common_slots = find_common_slots(compressed_calendar)
    ranked_slots = rank_slots(common_slots)

    print("\nRanked Meeting Slot Recommendations:")
    for slot in ranked_slots:
        print(
            f"{slot['day']}: {slot['start']} - {slot['end']} "
            f"(Score: {slot['score']})"
        )
