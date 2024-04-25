"""Pizza."""

import matplotlib.pyplot as plt
import streamlit as st

st.title("Streamlit App: Pizza Hawaii")

pizza_eaten = st.slider("How much pizza have you eaten?", 0, 100, 0)

sizes = [pizza_eaten, 100 - pizza_eaten]
labels = ["Pizza eaten", "Pizza left 2"]
colors = ["yellow", "red"]

fig, chart = plt.subplots()
chart.pie(
    sizes,
    labels=labels,
    colors=colors,
)

st.pyplot(fig)
