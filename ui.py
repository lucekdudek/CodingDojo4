import streamlit as st
from main import Peg, generate_hidden_code, feedback

MAPPING = {
    Peg.RED: "🔴",
    Peg.BLACK: "⚫️",
    Peg.YELLOW: "🟡",
    Peg.BLUE: "🔵",
    Peg.WHITE: "⚪️",
    Peg.GREEN: "🟢",
}
REV_MAPPING = {v: k for k, v in MAPPING.items()}

def feedback2(hidden_code, guess):
    result = feedback([REV_MAPPING[i] for i in hidden_code], [REV_MAPPING[i] for i in guess])
    return ''.join(MAPPING[i] for i in result)


st.header("Mastermind", divider="rainbow")
COLORS = list(MAPPING.values())

if "history" not in st.session_state:
    st.session_state["history"] = []
    st.session_state["hidden_code"] = [MAPPING[i] for i in generate_hidden_code()]


hidden_code = st.session_state["hidden_code"]
with st.expander("Cheat"):
    st.write(f"Hidden code: {'&nbsp;'.join(hidden_code)}")

assert len(hidden_code) == 4

# show history
for a, b in st.session_state["history"]:
    cols = st.columns([1, 1, 1, 1, 3])
    for i in range(4):
        cols[i].write(a[i])
    cols[4].write(f"Feedback: {b}")

if len(st.session_state["history"]) > 0 and (
    st.session_state["history"][-1][0] == list(hidden_code)
):
    st.success("You win!", icon="✅")
    st.balloons()
elif len(st.session_state["history"]) >= 10:
    st.error(f"You have run out of tries! The code was: {' '.join(hidden_code)}")
else:
    cols = st.columns([1, 1, 1, 1, 3])
    guess = []
    for i in range(4):
        g = cols[i].selectbox(f"color{i}", COLORS, label_visibility="collapsed")
        guess.append(g)

    if cols[4].button("Guess"):
        f = feedback2(hidden_code, guess)
        st.session_state["history"].append((guess, f))
        st.rerun()
