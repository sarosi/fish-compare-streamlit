import streamlit as st
from data import SPECIES_DATA


def run():
    st.header("Find Compatible Species for Your Tank")

    st.subheader("Set Your Tank Conditions")

    # -----------------------------
    # Sliders for water parameters
    # -----------------------------

    temperature = st.slider(
        "Temperature (°C)",
        min_value=10,
        max_value=35,
        value=24
    )

    ph = st.slider(
        "pH",
        min_value=4.0,
        max_value=9.0,
        value=7.0,
        step=0.1
    )

    hardness = st.slider(
        "Hardness (°dGH)",
        min_value=0,
        max_value=30,
        value=10
    )

    tank_size = st.slider(
        "Tank Size (Liters)",
        min_value=10,
        max_value=500,
        value=60,
        step=5
    )

    # -----------------------------
    # Filtering logic
    # -----------------------------

    compatible_species = []

    for species, params in SPECIES_DATA.items():

        temp_min, temp_max = params["Temperature (°C)"]
        ph_min, ph_max = params["pH"]
        hard_min, hard_max = params["Hardness (dGH)"]
        min_tank_size = params["Min Tank Size (L)"]

        if (
            temp_min <= temperature <= temp_max and
            ph_min <= ph <= ph_max and
            hard_min <= hardness <= hard_max and
            tank_size >= min_tank_size
        ):
            compatible_species.append(species)

    # -----------------------------
    # Output
    # -----------------------------

    st.subheader("Compatible Species")

    if compatible_species:
        for species in compatible_species:
            min_size = SPECIES_DATA[species]["Min Tank Size (L)"]
            st.success(f"{species} (Min Tank: {min_size} L)")
    else:
        st.error("No species match the selected conditions.")
