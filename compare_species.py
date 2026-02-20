import streamlit as st
import matplotlib.pyplot as plt
from data import SPECIES_DATA, PLACEHOLDER_IMAGE
from ui import load_css, species_card




def intersection(ranges):
    low = max(r[0] for r in ranges)
    high = min(r[1] for r in ranges)
    return (low, high) if low <= high else None


def run():
    load_css()

    st.header("Compare Species Parameters")

    st.subheader("Select Species")

    # -----------------------------
    # Build grouped options
    # -----------------------------

    CATEGORY_ICONS = {
        "Fish": "🐟",
        "Shrimp": "🦐",
        "Other": "🐌"
    }

    grouped_options = {}

    for species, data in SPECIES_DATA.items():
        category = data["Category"]
        grouped_options.setdefault(category, []).append(species)

    # Sort categories and species
    for category in grouped_options:
        grouped_options[category].sort()

    # Flatten into labeled list
    display_options = []
    species_lookup = {}

    for category in sorted(grouped_options.keys()):
        icon = CATEGORY_ICONS.get(category, "")
        for species in grouped_options[category]:
            label = f"{icon} {species}"
            display_options.append(label)
            species_lookup[label] = species


    # -----------------------------
    # Multiselect
    # -----------------------------

    selected_labels = st.multiselect(
        "Select species to compare",
        options=display_options,
        placeholder="Choose species..."
    )

    selected_species = [species_lookup[label] for label in selected_labels]


    if len(selected_species) < 1:
        st.warning("Please select at least one species.")
        return

    # Separate water parameters from tank size
    water_parameters = [
        "Temperature (°C)",
        "pH",
        "Hardness (dGH)"
    ]

    # -----------------------------
    # Overlap computation
    # -----------------------------

    st.subheader("Common Parameter Ranges")

    cols = st.columns(len(selected_species))

    st.subheader("Selected Species")

    for species in selected_species:
        data = SPECIES_DATA[species]
        image_path = data.get("Image") or PLACEHOLDER_IMAGE

        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(image_path, width=160)

            with col2:
                st.markdown(
                    f'<div class="card-title">{species}</div>',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="card-sub">Min Tank Size: {data["Min Tank Size (L)"]} L</div>',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="card-sub">Category: {data["Category"]}</div>',
                    unsafe_allow_html=True
                )

            st.markdown('</div>', unsafe_allow_html=True)


    for param in water_parameters:
        ranges = [SPECIES_DATA[s][param] for s in selected_species]
        result = intersection(ranges)

        if result:
            st.success(f"{param}: {result[0]} – {result[1]}")
        else:
            st.error(f"{param}: No common range")

    # -----------------------------
    # Minimal tank size
    # -----------------------------

    min_tank_size = max(
        SPECIES_DATA[s]["Min Tank Size (L)"]
        for s in selected_species
    )

    st.subheader("Minimal Tank Size Required")

    st.info(f"At least **{min_tank_size} liters**")

    # -----------------------------
    # Visualization
    # -----------------------------

    st.subheader("Visual Comparison")

    fig, axes = plt.subplots(len(water_parameters), 1, figsize=(10, 4 * len(water_parameters)))
    if len(water_parameters) == 1:
        axes = [axes]

    for ax, param in zip(axes, water_parameters):
        y_labels = []
        y_pos = []

        for i, s in enumerate(selected_species):
            r = SPECIES_DATA[s][param]
            ax.barh(i, r[1] - r[0], left=r[0], alpha=0.6)
            y_labels.append(s)
            y_pos.append(i)

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
