# Project Documentation  
## AI Meeting Scheduler Agent

---

## 1. Introduction
The AI Meeting Scheduler Agent is a rule-based intelligent system that helps determine the most suitable meeting time for multiple participants.  
It analyzes participant availability and time preferences to reduce scheduling conflicts and manual coordination.

---

## 2. Objective
The objective of this project is to:
- Minimize meeting scheduling latency
- Reduce manual effort in coordinating meetings
- Demonstrate agent-based decision making
- Optimize meeting time selection using preferences

---

## 3. System Overview
The system follows a simple agent pipeline:

1. Read availability data from a JSON file  
2. Compress calendar data by grouping availability day-wise  
3. Identify overlapping time slots among participants  
4. Apply time-based preference scoring  
5. Recommend the best meeting slot  

---

## 4. Input Data Format
The input is provided in JSON format.

Each participant includes:
- `person`: Name of the participant  
- `availability`: List of available time slots  
- `preference`: Preferred time of day  

### Example Input
```json
{
  "person": "Alice",
  "availability": [
    { "day": "Monday", "start": 10, "end": 12 }
  ],
  "preference": "morning"
}
```

---

## 5. Calendar Data Compression

Calendar compression is performed by grouping all availability slots by day.
This eliminates redundant information and simplifies overlap detection.

Benefits:

- Reduced complexity
- Faster decision making
- Cleaner scheduling logic

---

## 6. Scheduling Logic

For each day, the agent computes a common meeting slot by:
- Taking the maximum of all start times
- Taking the minimum of all end times
- A meeting slot is considered valid only if:
  start_time < end_time

---

## 7. Preference-Based Optimization

Each valid meeting slot is categorized into:
- Morning (9–12)
- Afternoon (12–16)
- Evening (16–19)

Slots are scored based on how many participant preferences match the time category.
Higher scores indicate better suitability.

---

## 8. Output

The system outputs ranked meeting slot recommendations in the command line.
Sample Output

🤖 AI Meeting Scheduler Recommendations:

-Monday | 11 - 12 | Score: 3

---

## 9. Error Handling

If no overlapping time slot exists, the agent correctly reports:
No common meeting slots found.

This ensures reliable and explainable behavior.

---

## 10. Limitations

- All participants must have overlapping availability
- Preferences are limited to time of day
- No real calendar integration

## 11. Future Enhancements

- Day-based preferences
- Priority-based participants
- Web interface (Streamlit / FastAPI)
- Integration with real calendar APIs

## 12. Conclusion

The AI Meeting Scheduler Agent demonstrates how agent-based reasoning and constraint optimization can be applied to real-world scheduling problems using simple and explainable logic.





