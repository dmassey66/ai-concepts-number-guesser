import streamlit as st

st.title("AI Number Guesser")
low, high = 1, 100
guess = (low + high) // 2
st.write(f"""
This is a stub demo. I would guess **{guess}** first and then adapt based on
feedback (higher/lower) using binary search + uncertainty notes.
""")
