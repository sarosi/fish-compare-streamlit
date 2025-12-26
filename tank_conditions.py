import streamlit as st
import matplotlib.pyplot as plt
from data import SPECIES_DATA


def run():
    st.header("Find Species by Tank Conditions")

    parameters = list(next(iter(SPECIES_DATA.values())).keys())

    st.sidebar.header("Tank Conditions")
    tank_conditions = {}

    for param in parameters:
        all_ranges = [SPECIES_DATA[s][param] for s in SPECIES_DATA]
        global_min = min(r[0] for r in all_ranges)
        global_max = max(r[1] for r in all_ranges)

        tank_conditions[param] = st.sidebar.slider(
            param,
            float(global_min),
            float(global_max),
            float((global_min + global_max) / 2),
            step=0.1
        )

    def species_fits(species_params):
        for param, value in tank_conditions.items():
            low, high = species_params[param]
            if not (low <= value <= high):
                return False
        return True

    st.subheader("Compatible Species")

    compatible = [
        s for s in SPECIES_DATA
        if species_fits(SPECIES_DATA[s])
    ]

    if compatible:
        for s in compatible:
            st.success(s)
    else:
        st.error("No species fit the selected tank conditions.")

    st.subheader("Tolerance Ranges vs Tank Conditions")

    fig, axes = plt.subplots(len(parameters), 1, figsize=(10, 4 * len(parameters)))
    if len(parameters) == 1:
        axes = [axes]

    for ax, param in zip(axes, parameters):
        for i, s in enumerate(SPECIES_DATA):
            r = SPECIES_DATA[s][param]
            ax.barh(i, r[1] - r[0], left=r[0], alpha=0.4)

        ax.axvline(tank_conditions[param], linestyle="--")
        ax.set_yticks(range(len(SPECIES_DATA)))
        ax.set_yticklabels(SPECIES_DATA.keys())
        ax.set_title(param)
        ax.set_xlabel(param)
        ax.grid(True)

    st.pyplot(fig)
