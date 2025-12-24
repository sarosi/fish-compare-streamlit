import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aquatic Species Compatibility", layout="wide")

# ----------------------------------
# Species data (editable / extensible)
# ----------------------------------

species_data = {
    "Neocaridina Shrimp": {
        "Temperature (°C)": (16, 26),
        "pH": (6.5, 8.0),
        "Hardness (dGH)": (4, 12),
    },
    "Gourami": {
        "Temperature (°C)": (22, 28),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (5, 15),
    },
    "Hillstream Loach": {
        "Temperature (°C)": (18, 24),
        "pH": (6.0, 7.5),
        "Hardness (dGH)": (4, 25),
    },
    "Otocinclus": {
        "Temperature (°C)": (20, 28),
        "pH": (5.5, 7.5),
        "Hardness (dGH)": (3, 15),
    },
    "Pfeffersalmler": {
        "Temperature (°C)": (20, 28),
        "pH": (5.0, 7.0),
        "Hardness (dGH)": (2, 10),
    },
}

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
    s for s in species_data
    if st.sidebar.checkbox(s, value=True)
]

if len(selected_species) < 2:
    st.warning("Please select at least two species.")
    st.stop()

parameters = species_data[selected_species[0]].keys()

# ----------------------------------
# Text summary
# ----------------------------------

st.subheader("Common Parameter Ranges")

for param in parameters:
    ranges = [species_data[s][param] for s in selected_species]
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
        r = species_data[s][param]
        ax.barh(i, r[1] - r[0], left=r[0], alpha=0.6)
        y_labels.append(s)
        y_pos.append(i)

    # Common overlap
    result = intersection([species_data[s][param] for s in selected_species])
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
