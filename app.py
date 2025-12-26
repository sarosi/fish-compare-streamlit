import streamlit as st
import matplotlib.pyplot as plt
from data import SPECIES_DATA

st.set_page_config(page_title="Aquatic Species Compatibility", layout="wide")

# ----------------------------------
# Species data (editable / extensible)
# ----------------------------------



# ----------------------------------
# Helper functions
# ----------------------------------

def intersection(ranges):
    low = max(r[0] for r in ranges)
    high = min(r[1] for r in ranges)
    return (low, high) if low <= high else None

# ----------------------------------
# UI
# ----------------------------------

st.title("Freshwater Species Parameter Compatibility")

st.sidebar.header("Select Species")
selected_species = [
    s for s in SPECIES_DATA
    if st.sidebar.checkbox(s, value=True)
]

if len(selected_species) < 2:
    st.warning("Please select at least two species.")
    st.stop()

parameters = SPECIES_DATA[selected_species[0]].keys()

# ----------------------------------
# Text summary
# ----------------------------------

st.subheader("Common Parameter Ranges")

for param in parameters:
    ranges = [SPECIES_DATA[s][param] for s in selected_species]
    result = intersection(ranges)

    if result:
        st.success(f"{param}: {result[0]} – {result[1]}")
    else:
        st.error(f"{param}: No common range")

# ----------------------------------
# Visualization
# ----------------------------------

st.subheader("Visual Comparison")

fig, axes = plt.subplots(len(parameters), 1, figsize=(10, 4 * len(parameters)))
if len(parameters) == 1:
    axes = [axes]

for ax, param in zip(axes, parameters):
    y_labels = []
    y_pos = []

    for i, s in enumerate(selected_species):
        r = SPECIES_DATA[s][param]
        ax.barh(i, r[1] - r[0], left=r[0], alpha=0.6)
        y_labels.append(s)
        y_pos.append(i)

    # Common overlap
    result = intersection([SPECIES_DATA[s][param] for s in selected_species])
    if result:
        ax.barh(len(selected_species), result[1] - result[0],
                left=result[0], color="green")
        y_labels.append("COMMON RANGE")
        y_pos.append(len(selected_species))

    ax.set_yticks(y_pos)
    ax.set_yticklabels(y_labels)
    ax.set_title(param)
    ax.grid(True)

st.pyplot(fig)
