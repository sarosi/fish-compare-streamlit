import streamlit as st


def load_css():
    st.markdown("""
    <style>
    .card {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
        margin-bottom: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .card-title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .card-sub {
        color: #555;
        font-size: 14px;
        margin-bottom: 3px;
    }
    </style>
    """, unsafe_allow_html=True)


def species_card(species_name, data, image_path):
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(image_path, width=160)

        with col2:
            st.markdown(
                f'<div class="card-title">{species_name}</div>',
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

        # Collapsible details section
        with st.expander("Water Parameters"):
            st.write(f"**Temperature (°C):** {data['Temperature (°C)'][0]} – {data['Temperature (°C)'][1]}")
            st.write(f"**pH:** {data['pH'][0]} – {data['pH'][1]}")
            st.write(f"**Hardness (°dGH):** {data['Hardness (°dGH)'][0]} – {data['Hardness (°dGH)'][1]}")

        st.markdown('</div>', unsafe_allow_html=True)
