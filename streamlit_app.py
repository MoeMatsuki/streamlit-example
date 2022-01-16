import altair as alt
import streamlit as st
import pandas as pd
import numpy as np

from streamlit_vega_lite import vega_lite_component, altair_component

hist_data = pd.DataFrame(np.random.normal(42, 10, (200, 1)), columns=["x"])

@st.cache
def altair_histogram():
    brushed = alt.selection_interval(encodings=["x"], name="brushed")

    return (
        alt.Chart(hist_data)
        .mark_bar()
        .encode(alt.X("x:Q", bin=True), y="count()")
        .add_selection(brushed)
    )

event_dict = altair_component(altair_chart=altair_histogram())

r = event_dict.get("x")
vega_lite_component()
if r:
    filtered = hist_data[(hist_data.x >= r[0]) & (hist_data.x < r[1])]
    st.write(filtered)
