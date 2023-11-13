import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

def generate_spiral_data(num_points, num_turns):
    indices = np.linspace(0, 1, num_points)
    theta = 2 * np.pi * num_turns * indices
    radius = indices

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    df = pd.DataFrame({
        "x": x,
        "y": y,
        "idx": indices,
        "rand": np.random.randn(num_points),
    })

    return df

def plot_spiral_chart(df):
    chart = alt.Chart(df, height=700, width=700).mark_point(filled=True).encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    )
    return st.altair_chart(chart)

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire ❤️.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

spiral_data = generate_spiral_data(num_points, num_turns)
plot_spiral_chart(spiral_data)
