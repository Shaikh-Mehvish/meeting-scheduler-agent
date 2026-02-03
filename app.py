import streamlit as st
from src.scheduler import (
    load_availability,
    compress_calendar,
    find_common_slots,
    rank_slots
)

st.set_page_config(page_title="AI Meeting Scheduler", layout="centered")

st.title("🤖 AI Meeting Scheduler Agent")
st.write(
    "This agent analyzes participant availability and time preferences "
    "to recommend the best meeting slot."
)

st.divider()

st.subheader("📂 Input Data")
st.write("Using availability data from `data/availability.json`")

if st.button("Schedule Meeting"):
    data = load_availability("data/availability.json")
    compressed_calendar = compress_calendar(data)
    common_slots = find_common_slots(compressed_calendar)
    ranked_slots = rank_slots(common_slots)

    st.divider()
    st.subheader("📊 Meeting Recommendations")

    if not ranked_slots:
        st.warning("No common meeting slots found.")
    else:
        for slot in ranked_slots:
            st.success(
                f"📅 {slot['day']} | ⏰ {slot['start']} - {slot['end']} "
                f"| ⭐ Score: {slot['score']}"
            )

st.divider()
st.caption("AI Meeting Scheduler • Built with Python & Streamlit")
